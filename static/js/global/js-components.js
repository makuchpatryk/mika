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

        var vueElements = document.querySelectorAll('*[data-init_vue]');
        var arr = [];
        for (var i = 0, len = vueElements.length; i < len; i++)
        {
            var vue_mount_point = $(vueElements[i]).data('init_vue'), instance;

            if (vue_mount_point in document._scd['components'])
            {
                continue;
            }
            // this will prevent vue from reinitialisation of otherwise alive objects
            document._scd['components'][vue_mount_point] = 'initialising...';

            instance  = new Vue({
                el: vue_mount_point,
                mounted: function () {
                    // $('body').trigger('initComponents', ['vue-init']);
                }
            })

            document._scd['components'][vue_mount_point] = instance;
        }
    })

});
