from django import forms
from .models import Choice


class ResponseForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.all())
    comment = forms.CharField()
