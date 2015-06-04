from django import forms
from .models import Choice


class ResponseForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.widgets.RadioSelect)
    comment = forms.CharField(widget=forms.widgets.Textarea)
