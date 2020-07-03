from django import forms
from .models import Short_Url


class Url_Form(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'https://long_uneccesary_url.com/stringOf_characters',
            'name': 'Long_URL',
            'aria_label': 'Large',
            'aria-describedby': 'inputGroup-sizing-sm',

        }), label='')

    class Meta:
        model = Short_Url
        fields = ['long_url',]
