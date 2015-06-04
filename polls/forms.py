from django import forms
from django.forms.models import inlineformset_factory
from .models import Response, Poll, Choice


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


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

InlineChoiceFormset = inlineformset_factory(
    Poll,
    Choice,
    fields='__all__',
    can_delete=False,
    extra=10,
    max_num=10,
)