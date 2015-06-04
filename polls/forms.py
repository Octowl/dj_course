from django import forms
from .models import Response, Choice


# class ResponseForm(forms.Form):
#     choice = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.widgets.RadioSelect)
#     comment = forms.CharField(widget=forms.widgets.Textarea)

class ResponseForm(forms.ModelForm):
    # choice = forms.ModelChoiceField(
    #     queryset=Choice.objects.all(),
    #     widget=forms.RadioSelect,
    #     empty_label=None)

    class Meta:
        model = Response
        fields = '__all__'
        widgets = {
            'choice': forms.RadioSelect,
        }