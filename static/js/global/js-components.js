$(function() {
    $('body').on('initComponents', function(e)
    {
        $('*[data-init_js]').each(function(idx, el)
        {
            var event_name = $(el).data('init_js');
            already_initialised = $(el).data('already_initialised');
            if (already_initialised)
            {
                return;
            }
            if (event_name)
            {
                $('body').trigger(event_name, [$(el)]);
                $(el).data('already_initialised', true);
            }
        })
    })

});
