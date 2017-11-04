from django import forms
from django.core.validators import *
from django.core.exceptions import *


class Login(forms.Form):
    login = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class AddFileForm(forms.Form):
    server_path = forms.CharField(max_length=128, required=False)
    disk_file = forms.FileField(required=False)

    def clean(self):
        # if more or less than one was given (XOR)
        if not ((self.cleaned_data['server_path'] and
                not self.cleaned_data['disk_file'])

                or (not self.cleaned_data['server_path']
                    and self.cleaned_data['disk_file'])):
            raise forms.ValidationError({'server_path': 'Fill only '
                                                        'one of the fields'})

        return self.cleaned_data
