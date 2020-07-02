from django import forms
from .models import Short_Url


class Url_Form(forms.ModelForm):

    class Meta:
        model = Short_Url
        fields = ['long_url']
