from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from upload.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from tcs.decorators import *

def notApprovedorSuggested(function):
	def wrap(request, *args, **kwargs):
		taskModel= Timeline.objects.get(Q(teamName=kwargs['team']) & Q(task=kwargs['task']))
		user=User.objects.get(username=kwargs['uploadedBy'])
		file=File.objects.get(Q(name=kwargs['filename']) & Q(uploadedBy=user) & Q(task=taskModel))
		if Suggestion.objects.filter( Q(file=file) & Q(suggestedBy=request.user) ) or Approval.objects.filter( Q(file=file) & Q(approvedBy=request.user) ):
			raise PermissionDenied
		else:
			return function(request, *args, **kwargs)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def approvedorSuggestedorDeveloper(function):
	def wrap(request, *args, **kwargs):
		member = TeamMember.objects.get(Q(teamName = kwargs['team'] ) & Q(userName = request.user ))
		dev=Role.objects.get(role="Developer")
		if member.role == dev:
			return function(request, *args, **kwargs)
		else:
			taskModel= Timeline.objects.get(Q(teamName=kwargs['team']) & Q(task=kwargs['task']))
			user=User.objects.get(username=kwargs['uploadedBy'])
			file=File.objects.get(Q(name=kwargs['filename']) & Q(uploadedBy=user) & Q(task=taskModel))
			if Suggestion.objects.filter( Q(file=file) & Q(suggestedBy=request.user) ) or Approval.objects.filter( Q(file=file) & Q(approvedBy=request.user) ):
				return function(request, *args, **kwargs)
			else:
				raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap
