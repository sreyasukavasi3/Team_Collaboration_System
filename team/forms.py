from django import forms
from .models import *
from django.db.models import Q
from django.forms import ModelChoiceField

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('teamName', 'directoryLink','teamLeader')

class TeamMemberForm(forms.ModelForm):
	Role = ModelChoiceField(queryset=Role.objects.filter(~Q(role='Team Leader')), empty_label=None)
	class Meta:
		model = TeamMember
		fields = ('userName',)

class TimelineForm(forms.ModelForm):

    class Meta:
        model = Timeline
        fields = ('deadline', 'task','taskDetails')

class GradeForm(forms.Form):
    grade = forms.CharField(max_length=100)
