from django import forms
from mailing.models import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('user_email',)
