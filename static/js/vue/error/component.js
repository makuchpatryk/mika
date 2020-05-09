$(document).bind('ready', function() {
    Vue.component('vue-error-component', {
        template: '#vue-error-component',
        props: [
            'errors'
        ],
        computed: {
            hasErrorsToDisplay: function () {
                return this.errors.length ? true : false
            }
        }
    })
})