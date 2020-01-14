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
            "placeholder": "Twoj emial...", "class": "form-control"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Twoj tytul...", 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Twoj wiadomość...", 'class': 'form-control'}))

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

class PreorderForm(forms.Form):
    email = forms.EmailField(
        required=True, label="Email", max_length=255,
        help_text="Powinien byc wlasciwy adres email", error_messages={
            "invalid": "Adres email jest nie wlasciwy",
            "required": "Prosze podaj swoj adres email",
        }, widget=forms.TextInput(attrs={
            "placeholder": "Twoj emial...", "class": "form-control"}))
    # item = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ile sztuk...", 'class': 'form-control'}), initial=1)
    adres_to_send = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Adres do wysylki...", 'class': 'form-control', 'required': "required"}))
    name_on_disk = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Imie do dedykacją...", 'class': 'form-control', 'required': "required"}))

    def send_email(self):
        sub = '{} : {} : {}'.format('Preorder',self.cleaned_data['email'],  self.cleaned_data['name_on_disk'])
        msg = '{}'.format(self.cleaned_data['adres_to_send'])
        mail = send_mail(
            sub,
            msg,
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return mail
