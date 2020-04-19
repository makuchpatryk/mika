import gulp       from 'gulp';
import plugins    from 'gulp-load-plugins';
import browser    from 'browser-sync';
import rimraf     from 'rimraf';
import panini     from 'panini';
import yargs      from 'yargs';
import lazypipe   from 'lazypipe';
import inky       from 'inky';
import fs         from 'fs';
import siphon     from 'siphon-media-query';
import path       from 'path';
import merge      from 'merge-stream';
import colors     from 'colors';
import whitespace from 'gulp-whitespace';
import glob       from 'gulp-sass-glob';

const $ = plugins();

// Look for the --production flag
const PRODUCTION = !!(yargs.argv.production);

/*===================================
=            EMAIL SHIZZLE            =
===================================*/

// Build the "dist" folder by running all of the above tasks
gulp.task('build:emails',
  gulp.series(emailClean, emailPages, emailSass, emailInline, emailWhitespace));

// Build emails, run the server, and watch for file changes
gulp.task('emails',
  gulp.series('build:emails', serverEmails, watchEmails));

/*----------  TASKS  ----------*/

// Delete the "dist" folder - this happens every time a build starts
function emailClean(done) {
  rimraf('templates/emails', done);
}

// Compile layouts, pages, and partials into flat HTML files
// Then parse using Inky templates
function emailPages() {
  return gulp.src('emails/src/pages/**/*.html')
    .pipe(panini({
      root: 'emails/src/pages',
      layouts: 'emails/src/layouts',
      partials: 'emails/src/partials',
      helpers: 'emails/src/helpers'
    }))
    .pipe(inky())
    .pipe(gulp.dest('templates/emails'));
}

// Reset Panini's cache of layouts and partials
function resetEmails(done) {
  panini.refresh();
  done();
}

function emailWhitespace() {
    return gulp.src('dist/scoop-emails/*.html')
    .pipe(whitespace({
        removeTrailing: true
    }))
    .pipe(gulp.dest('dist/scoop-emails/'));
}

// Compile Sass into CSS
function emailSass() {
  return gulp.src('emails/src/assets/scss/main.scss')
    .pipe($.if(!PRODUCTION, $.sourcemaps.init()))
    .pipe($.sass({
      includePaths: ['node_modules/foundation-emails/scss']
    }).on('error', $.sass.logError))
    .pipe($.if(!PRODUCTION, $.sourcemaps.write()))
    .pipe(gulp.dest('templates/emails/css'));
}

// Inline CSS and minify HTML
function emailInline() {
  return gulp.src('templates/emails/**/*.html')
    .pipe($.if(PRODUCTION, emailInliner('templates/emails/css/main.css')))
    .pipe(gulp.dest('templates/emails'));
}

// Start a server with LiveReload to preview the site in
function serverEmails(done) {
  browser.init({
    server: 'templates/emails',
    open: false
  });
  done();
}

// Watch for file changes
function watchEmails() {
  gulp.watch('emails/src/pages/**/*.html').on('change', gulp.series(emailPages, emailInline, browser.reload));
  gulp.watch(['emails/src/layouts/**/*', 'emails/src/partials/**/*']).on('change', gulp.series(emailPages, emailInline, browser.reload));
  gulp.watch(['emails/src/assets/scss/**/*.scss']).on('change', gulp.series(emailSass, emailPages, emailInline, browser.reload));
}

// Inlines CSS into HTML, adds media query CSS into the <style> tag of the email, and compresses the HTML
function emailInliner(css) {
  var css = fs.readFileSync(css).toString();
  var mqCss = siphon(css);

  var pipe = lazypipe()
    .pipe($.inlineCss, {
      applyStyleTags: false,
      removeStyleTags: false,
      removeLinkTags: false
    })
    .pipe($.replace, '<!-- <style> -->', `<style>${mqCss}</style>`)
    .pipe($.replace, '<link rel="stylesheet" type="text/css" href="css/app.css">', '')
    .pipe($.htmlmin, {
      collapseWhitespace: true,
      minifyCSS: true
    });

  return pipe();
}

/*====================================
=            SITE SHIZZLE            =
====================================*/

// Build main site and watch SASS and JS files for change
gulp.task('default',
  gulp.series(siteSass, siteServer, siteWatch));

gulp.task('sass',
  gulp.series(siteSass));

const outputStyle = yargs.argv.production ? 'compressed' : 'expanded';

/*----------  TASKS  ----------*/

function siteSass() {
    return gulp.src('static/sass/**/*.scss')
    .pipe(glob())
    .pipe($.if(!yargs.argv.production, $.sourcemaps.init()))
    .pipe($.sass({outputStyle: outputStyle}).on('error', $.sass.logError))
    .pipe($.if(!yargs.argv.production, $.sourcemaps.write()))
    .pipe(gulp.dest('static/css'))
    .pipe(browser.stream());
}


function siteServer(done) {
    browser.init({
        proxy: 'localhost:8000',
        open: false
    });
    done();
}

function siteWatch() {
    gulp.watch(['static/sass/**/*.scss']).on('change', siteSass);
    gulp.watch(['static/js/**/*.js']).on('change', browser.reload);
}

