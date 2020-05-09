$(document).bind('ready', function() {
    Vue.component('vue-comment-form', {
        template: '#vue-comment-form',
        mixins: [VueFormMixin],
        props: {
            postId: {
                type: Number,
                default: null
            },
        },
        data: function ()
        {
            var formData = this.getFormData();
            return {
                obj: {
                    user: formData.user,
                    content: formData.content,
                },
                error: {
                    general: [],
                    name: [],
                    content: [],
                },
            }
        },
        mounted: function()
        {
        },
        methods: {
            getFormData: function()
            {
                var form = {
                    name: '',
                    content: '',
                };

                return form;
            },
            canComment: function()
            {
                if (getCookie('commentPost_' + this.postId))
                {
                    return false;
                };
                return true
            },
            postComment: function () {
                var vm = this;
                vm.showPostPreloader(vm.$el);
                
                $.ajax({
                    method: 'POST',
                    url: document._scd['routing']['comment_post'],
                    data: {
                        'post_id': vm.postId,
                        'name': vm.obj.name,
                        'content': vm.obj.content,
                        },
                }).done(function(response) {
                    setCookie('commentPost_' + vm.postId, false);
                    vm.hidePostPreloader(vm.$el);
                    window.location.reload();
                })
                .fail(function(response) {
                    console.log(response, 'fail');
                    vm.handleErrors(response);
                    vm.hidePostPreloader(vm.$el);
                });
            }
        }
    })
})