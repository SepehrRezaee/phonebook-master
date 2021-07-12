from django import forms
from . import models


class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
        )
