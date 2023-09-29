from django import forms
from .models import *

class ModelFormWithFileField(forms.ModelForm):

    class Meta:
        model = File
        fields = ('name', 'file')

class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        fields = ('suggestion',)

class ApprovalForm(forms.ModelForm):

    class Meta:
        model = Approval
        fields = ('grade',)
