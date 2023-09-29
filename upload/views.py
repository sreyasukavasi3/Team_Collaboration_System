from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from team.models import *
from . import models
from django.shortcuts import redirect
from .models import File
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from tcs.decorators import *
from .decorators import *

@login_required
@userIsMember
@userIsDeveloper
def index(request,team,task):
	if Timeline.objects.filter(Q(teamName=team) & Q(task=task) & Q(grade=None)):
		if request.method == 'POST':
			form = ModelFormWithFileField(request.POST, request.FILES)
			if form.is_valid():
				file=form.save(commit=False)
				file.uploaded_at=timezone.now()
				file.teamName=Team.objects.get(teamName=team)
				file.task=Timeline.objects.get(Q(teamName=team) & Q(task=task))
				file.file.name = team+"/"+task+"/"+request.user.username+"/"+file.name+"."+file.file.name.split(".")[-1]
				file.uploadedBy = request.user
				if File.objects.filter(Q(name=file.name) & Q(task=file.task) & Q(uploadedBy=file.uploadedBy)):
					return render(request, 'upload.html', {'form': form,'name1':team,'task1':task})
					file.save()
					return redirect('viewTimeline',team=team)
		else:
			form = ModelFormWithFileField()
			return render(request, 'upload.html', {'form': form,'name1':team,'task1':task})
	else:
		return HttpResponse("Already Graded")

@login_required
@userIsMember
def view(request,team,task):
	taskModel= Timeline.objects.get(Q(teamName=team) & Q(task=task))
	member = TeamMember.objects.get(Q(teamName =team ) & Q(userName = request.user ))
	dev=Role.objects.get(role="Developer")
	tes=Role.objects.get(role="Tester")
	tl=Role.objects.get(role="Team Leader")

	if member.role == dev:
		pfiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved=None))
		afiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved='yes'))
		rfiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved='no'))

	if member.role == tes:
		files=File.objects.filter(Q(teamName=team) & Q(task=taskModel))
		pfiles=[]
		afiles=[]
		rfiles=[]
		for file in files:
			if Suggestion.objects.filter( Q(file=file) & Q(suggestedBy=request.user) ):
				rfiles.append(file)
			elif Approval.objects.filter( Q(file=file) & Q(approvedBy=request.user) ):
				afiles.append(file)
			else:
				pfiles.append(file)
	if member.role == tl:
		pfiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved=None))
		afiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved='yes'))
		rfiles=File.objects.filter(Q(teamName=team) & Q(task=taskModel) & Q(approved='no'))

	root = settings.MEDIA_URL
	return render(request, 'view.html', {'pendingFiles':pfiles,'acceptedFiles':afiles,'rejectedFiles':rfiles , 'root':root,})

@login_required
@userIsMember
@approvedorSuggestedorDeveloper
def viewSuggestions(request,team,task,filename,uploadedBy):
	taskModel= Timeline.objects.get(Q(teamName=team) & Q(task=task) )
	user= User.objects.get(username=uploadedBy)
	file=File.objects.get(Q(teamName=team) & Q(task=taskModel) & Q(name=filename) & Q(uploadedBy=user))
	suggestions = Suggestion.objects.filter(file=file)
	return render(request, 'viewSuggestions.html', {'suggestions':suggestions,})

@login_required
@userIsMember
@userIsTester
@notApprovedorSuggested
def suggest(request,team,task,filename,uploadedBy):
	if request.method == 'POST':
		taskModel= Timeline.objects.get(Q(teamName=team) & Q(task=task) )
		user= User.objects.get(username=uploadedBy)
		file=File.objects.get(Q(teamName=team) & Q(task=taskModel) & Q(name=filename) & Q(uploadedBy=user))
		form = SuggestionForm(request.POST)
		if form.is_valid():
			suggestion = form.save(commit=False)
			suggestion.suggestedAt=timezone.now()
			suggestion.file=file
			suggestion.suggestedBy=request.user
			suggestion.save()
			return redirect('view',team=team,task=task)
	else:
		form = SuggestionForm()
	return render(request, 'suggest.html', {'form':form,})

@login_required
@userIsMember
@approvedorSuggestedorDeveloper
def viewApprove(request,team,task,filename,uploadedBy):
	taskModel= Timeline.objects.get(Q(teamName=team) & Q(task=task) )
	user= User.objects.get(username=uploadedBy)
	file=File.objects.get(Q(teamName=team) & Q(task=taskModel) & Q(name=filename) & Q(uploadedBy=user))
	approvals = Approval.objects.filter(file=file)
	return render(request, 'viewApprovals.html', {'approvals':approvals,})

@login_required
@userIsMember
@userIsTester
@notApprovedorSuggested
def approve(request,team,task,filename,uploadedBy):
	taskModel= Timeline.objects.get(Q(teamName=team) & Q(task=task))
	user= User.objects.get(username=uploadedBy)
	file=File.objects.get(Q(teamName=team) & Q(task=taskModel) & Q(name=filename) & Q(uploadedBy=user))
	if request.method == 'POST':
		form = ApprovalForm(request.POST)
		if form.is_valid():
			approve = form.save(commit=False)
			approve.approvedBy=request.user
			approve.approvedAt=timezone.now()
			approve.file=file
			approve.save()
			t=Role.objects.get(role='Tester')
			testers=TeamMember.objects.filter(Q(teamName=team) & Q(role=t))
			approved=1
			for tester in testers:
				if Approval.objects.filter( Q(file=file) & Q(approvedBy=tester.userName) ):
					pass
				else:
					approved=0
					break
			if approved==1:
				file.approved='yes'
				file.save()

			return redirect('view',team=team,task=task)
	else:
		form = ApprovalForm()
	return render(request, 'approve.html', {'form':form,})
