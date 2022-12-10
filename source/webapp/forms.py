from django import forms
from django.forms import widgets
from webapp.models import Pull, Choice, Answer


class PullForm(forms.ModelForm):
    class Meta:
        model = Pull
        fields = ['survey']
        widgets = {'survey': widgets.Textarea}


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['option_fk']
        widgets = {'option_fk': widgets.RadioSelect}
