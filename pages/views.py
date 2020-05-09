import os

from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .forms import NameForm, OrderForm, OrderPaymentForm
from django.contrib import messages
from django.core.cache import cache
from django.core.paginator import Paginator
from django.core.mail import send_mail

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

from django.conf import settings
from . import models
from django.templatetags.static import static
from django.views.decorators.http import require_http_methods

from library import exceptions, logic

from django.http import HttpResponse
from .models import Snippet
from django.forms.models import model_to_dict


class IndexPageView(FormView):
    template_name = 'index.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_success')

    def form_valid(self, form):
        order = create_order(form)
        if order:
            emial = form.send_email()
            if emial:
                return super().form_valid(form)
        return HttpResponseRedirect(reverse('order_fail'))

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class AlbumsPylPageView(FormView):
    template_name = 'albums/pyl.html'
    form_class = OrderForm


    def get_success_url(self):
        return reverse('order_success')

    def form_valid(self, form):
        order = create_order(form)
        if order:
            emial = form.send_email()
            if emial:
                return super().form_valid(form)
        return HttpResponseRedirect(reverse('order_fail'))

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = NameForm
    success_url = '/'

    def form_valid(self, form):
        emial = form.send_email()
        if emial:
            return render(self.request, 'contact.html', {
                'form': form, 'message_sent': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AlbumsAlmagestPageView(TemplateView):
    template_name = 'albums/almagest.html'

class AlbumsAwePageView(TemplateView):
    template_name = 'albums/awe.html'

class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class EventPageView(TemplateView):
    template_name = 'event.html'


class GalleryView(TemplateView):
    template_name = 'gallery-main.html'


def feed(request):
    posts = models.Post.objects.all().order_by('-ctime')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, "blog/feed.html", context)


def post(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, "blog/post.html", context)


def akustycznie(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/akustycznie/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'akustycznie'}
    return render(request, "gallery/gallery.html", context)


def koncert(request):
    path = settings.STATICFILES_DIRS[0]

    img_list = os.listdir(path + '/img/gallery/koncert/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'koncert'}
    return render(request, "gallery/gallery.html", context)

def Sesja_2016(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2016/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'sesja_2016'}
    return render(request, "gallery/gallery.html", context)


def Sesja_2017(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2017/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'sesja_2017'}
    return render(request, "gallery/gallery.html", context)


def Sesja_2019(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2019/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'sesja_2019'}
    return render(request, "gallery/gallery.html", context)


def Sesja_2020(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2020/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'sesja_2020'}
    return render(request, "gallery/gallery.html", context)


def sesja_ayz(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_ayz/')
    paginator = Paginator(img_list, settings.GALLERY_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj' : page_obj, 'folder': 'sesja_ayz'}
    return render(request, "gallery/gallery.html", context)


def create_order(form):
    try:
        order = models.Order()
        order.name = form.cleaned_data['subject']
        order.email = form.cleaned_data['email']
        order.phone_number = form.cleaned_data['number']
        order.adres_to_send = form.cleaned_data['adres_to_send']
        order.status = models.Order.ORDERED
        order.save()
    except:
        return False
    return True


def sent_confimation(request, pk):

    if request.user.is_staff:
        email = request.GET.get('email', '')
        if not email:
            return messages.error(request, 'Error there is not email.')

        order = models.Order.objects.get(pk=pk)
        order.done = True
        order.status = models.Order.COMPLETED
        order.save()

        send_mail(
            "tomashmika.com : Twoje Zamowienie",
            "twoje zamowienie zostalo wyslane.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    messages.success(request, 'Sent Confirmation.')

    return HttpResponseRedirect(reverse('admin:pages_order_changelist'))


# Order
class OrderFormView(FormView):
    template_name = 'order/form.html'
    form_class = OrderPaymentForm
    order_id = None

    def get_success_url(self):
        return reverse('order_payment', kwargs={'order_id': self.order_id})

    def form_valid(self, form):
        try:
            self.order_id = logic.create_order_payment(form)
        except Exception:
            return HttpResponseRedirect(reverse('order_fail'))

        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)
        # return HttpResponseRedirect(reverse('order_fail'))


@require_http_methods(["GET"])
def order_payment(request):
    msg_error = 'Wystapil blad. Jeżeli złozyleś zamowie proszę skontaktuj sie z nami.'
    context = {
        'payment_display': True
    }
    if not request.user.is_staff:
        context['payment_display'] = False
        messages.error(request, msg_error)
    # if request.method == "GET":
    #     try:
    #         order = models.OrderPayment.objects.get(pk=order_id)
    #         print(order)

    #         if order.status != models.OrderPayment.ORDERED:
    #             raise exceptions.MikaException()
    #         context['order'] = model_to_dict(order)
    #         context['payment_display'] = True
    #     except ObjectDoesNotExist:
    #         raise Http404
    #     except ValueError:
    #         messages.error(request, msg_error)
    #     except exceptions.Exception:
    #         messages.error(request, msg_error)
    # else:
    #     messages.error(request, msg_error)
    return render(request, "order/payment.html", context)


@require_http_methods(["GET"])
def order_success(request):
    context = {}
    return render(request, "order/success.html", context)


@require_http_methods(["GET"])
def order_fail(request):
    context = {}
    return render(request, "order/fail.html", context)


@require_http_methods(["GET"])
def order_cancel(request):
    context = {}
    return render(request, "order/cancel.html", context)


def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse('the detailview for slug of {slug}'.format())
