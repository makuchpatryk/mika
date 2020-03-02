from django import forms
from django.core.mail import send_mail
from django.conf import settings


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
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
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
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return mail
