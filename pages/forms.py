from django import forms
from django.core.mail import send_mail
from django.conf import settings

from library import forms as lib_forms, logic


class NameForm(forms.Form):
    email = forms.EmailField(
        required=True, label="Email", max_length=255,
        help_text="Powinien byc wlasciwy adres email", error_messages={
            "invalid": "Adres email jest nie wlasciwy",
            "required": "Prosze podaj swoj adres email",
        }, widget=forms.TextInput(attrs={
            "placeholder": "Twój email...", "class": "form-control"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Temat...", 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Twoja wiadomość...", 'class': 'form-control'}))

    def send_email(self):
        sub = '{} : {} : {}'.format('Contact',self.cleaned_data['email'],  self.cleaned_data['subject'])
        mail = send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIVER_USER],
            fail_silently=False,
        )
        return mail


class OrderForm(forms.Form):
    email = forms.EmailField(
        required=True, label="Email", max_length=255,
        help_text="Powinien byc wlasciwy adres email", error_messages={
            "invalid": "Adres email jest nie wlasciwy",
            "required": "Prosze podaj swoj adres email",
        }, widget=forms.TextInput(attrs={
            "placeholder": "Twój email...", "class": "form-control"}))
    # item = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ile sztuk...", 'class': 'form-control'}), initial=1)
    adres_to_send = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Adres do wysyłki...", 'class': 'form-control', 'required': "required"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nazwisko...", 'class': 'form-control', 'required': "required"}))
    number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Numer kontaktowy...", 'class': 'form-control', 'required': "required"}))

    def send_email(self):
        sub = '{} : {} : {}'.format('Order',self.cleaned_data['email'],  self.cleaned_data['subject'])
        msg = '{}, numer: {}'.format(self.cleaned_data['adres_to_send'], self.cleaned_data['number'])
        mail = send_mail(
            sub,
            msg,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIVER_USER],
            fail_silently=False,
        )
        return mail


class OrderPaymentForm(lib_forms.FormBase):
    email = forms.EmailField(
        required=True, label="Email", max_length=255,
        help_text="Powinien byc wlasciwy adres email", error_messages={
            "invalid": "Adres email jest nie wlasciwy",
            "required": "Prosze podaj swoj adres email",
        }, widget=forms.TextInput(attrs={
            "placeholder": "Twój email...", "class": "form-control"}))
    name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Imię", 'class': 'form-control'}), required=False)
    surname = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Nazwisko", 'class': 'form-control'}), required=False)
    address_1 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Adres – wiersz 1", 'class': 'form-control'}), required=False)
    address_2 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Adres – wiersz 2", 'class': 'form-control'}), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Miejscowość", 'class': 'form-control'}), required=False)
    state = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Województwo", 'class': 'form-control'}), required=False)
    postcode = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Kod pocztowy", 'class': 'form-control'}), required=False)
    transation_id = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "...",
            'class': 'form-control'}))

    def send_email(self):
        """
        sending email to tomek
        """
        sub = '{} : {}'.format(
            'Order',self.cleaned_data['email'])
        msg = 'Imię i Nazwisko: {} {}, Miejscowość: {}, Numer: {}'.format(
            self.cleaned_data['name'],
            self.cleaned_data['name'],
            self.cleaned_data['city'],
            self.cleaned_data['number'],
            )
        mail = send_mail(
            sub,
            msg,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIVER_USER],
            fail_silently=False,
        )
        return mail


class CommentPostForm(lib_forms.FormBase):
    post_id = forms.IntegerField(widget=forms.TextInput(
        attrs={"placeholder": "Imię", 'class': 'form-control'}), required=True)
    name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Imię", 'class': 'form-control'}), required=True)
    content = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Nazwisko", 'class': 'form-control'}), required=True)

    def send_email(self):
        post = logic.get_post_by_uid(pk=self.cleaned_data['post_id'])
        sub = '{} : {} : {}'.format(
            self.cleaned_data['name'],
            'skomentowal Post ',
            post.title)
        mail = send_mail(
            sub,
            self.cleaned_data['content'],
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIVER_USER],
            fail_silently=False,
        )
        return mail