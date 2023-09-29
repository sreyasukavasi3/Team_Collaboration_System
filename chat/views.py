from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from django.utils import timezone
from .models import DirectMessage,GroupMessage
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import UsernameForm,DirectMessageForm,GroupMessageForm
from django import forms
from team.models import TeamMember
from django.contrib.auth.decorators import login_required
from tcs.decorators import *

@login_required
def index(request):
	chats=DirectMessage.objects.filter(Q(sentFrom=request.user) |  Q(sentTo=request.user)).order_by('created_date').reverse()
	chatList=[]
	chattedWith=set()
	companion=""
	for chat in chats:
		if chat.sentTo==request.user:
			companion=chat.sentFrom
		else:
			companion=chat.sentTo
		if companion not in chattedWith:
			chattedWith.add(companion)
			chatList.append(chat)


	teamObj=TeamMember.objects.filter(Q(userName=request.user))
	teams=[]
	for team in teamObj:
		teams.append(team.teamName)
	groupChats=[]
	for team in teams:
		groupChats.append(GroupMessage.objects.filter(Q(sentTo=team)).order_by('-created_date')[:1])
	return render(request, 'chatHistory.html', {'chats':chatList, 'groupChats':groupChats, 'user':request.user})

@login_required
def chatNow(request):
	if request.method == "POST":
		form = DirectMessageForm(request.POST)
		if form.is_valid():
			chat=form.save(commit=False)
			chat.created_date=timezone.now()
			chat.sentFrom=request.user
			chat.save()			
			return redirect('continueChat',name=chat.sentTo)
	else:
		form=DirectMessageForm()
	return render(request, 'message.html', {'form': form})

@login_required
@userIsMember
def groupChatNow(request):
	if request.method == "POST":
		form = GroupMessageForm(request.POST)
		if form.is_valid():
			chat=form.save(commit=False)
			chat.created_date=timezone.now()
			chat.sentFrom=request.user
			chat.save()			
			return redirect('continueGroupChat',name=chat.sentTo)
	else:
		form=GroupMessageForm()
	return render(request, 'message.html', {'form': form})

@login_required
def continueChat(request,name):
	if request.method == "POST":
		form = DirectMessageForm(request.POST)
		if form.is_valid():
			chat=form.save(commit=False)
			chat.created_date=timezone.now()
			chat.sentFrom=request.user
			chat.save()			
			return redirect('continueChat',name=name)	
	else:
		nameId=User.objects.get(username=name)
		chats=DirectMessage.objects.filter((Q(sentFrom=request.user) &  Q(sentTo=nameId)) | (Q(sentFrom=nameId) &  Q(sentTo=request.user))).order_by('created_date')
		form=DirectMessageForm(initial={'sentTo':nameId})
		form.fields['sentTo'].widget = forms.HiddenInput()
	return render(request, 'message.html', {'form': form,'chats':chats,'name':name})

@login_required
@userIsMember
def continueGroupChat(request,name):
	if request.method == "POST":
		form = GroupMessageForm(request.POST)
		if form.is_valid():
			chat=form.save(commit=False)
			chat.created_date=timezone.now()
			chat.sentFrom=request.user
			chat.save()			
			return redirect('continueGroupChat',name=name)	
	else:
		chats=GroupMessage.objects.filter(Q(sentTo=name)).order_by('created_date')
		form=GroupMessageForm(initial={'sentTo':name})
		form.fields['sentTo'].widget = forms.HiddenInput()
	return render(request, 'message.html', {'form': form,'chats':chats,'name':name})
