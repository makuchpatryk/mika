from django import forms
from django.core.mail import send_mail
from django.conf import settings


class NameForm(forms.Form):
    email = forms.EmailField(
        required=True, label="Email", max_length=255,
        help_text="Should be a valid email address", error_messages={
            "invalid": "Email address is not valid",
            "required": "Please enter an email address",
        }, widget=forms.TextInput(attrs={
            "placeholder": "Email", "class": "form-control"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your subject", 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your message", 'class': 'form-control'}))

    def send_email(self):
        mail = send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return mail

class PreorderForm(NameForm):
    def send_email(self):
        sub = ''.format('Preorder : ', self.cleaned_data['subject'])
        mail = send_mail(
            sub,
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return mail
