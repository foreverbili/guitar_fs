from django import forms
from gtpxz import models

class GtpForm(forms.ModelForm):
    class Meta:
        model = models.Gtp
        fields = ('name','cover','gtp')
