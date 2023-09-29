from django import forms
from .models import DirectMessage,GroupMessage
from django.contrib.auth.models import User

class DirectMessageForm(forms.ModelForm):

    class Meta:
        model = DirectMessage
        fields = ('sentTo','message',)

class GroupMessageForm(forms.ModelForm):

    class Meta:
        model = GroupMessage
        fields = ('sentTo','message',)

class UsernameForm(forms.ModelForm):

    class Meta:
        model = DirectMessage
        fields = ('sentTo',)