from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from team.models import *
from django.db.models import Q

def userIsTeamLeader(function):
    def wrap(request, *args, **kwargs):
        team = Team.objects.get(teamName = kwargs['team'])
        if team.teamLeader== request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def userIsDeveloper(function):
    def wrap(request, *args, **kwargs):
        member = TeamMember.objects.get(Q(teamName = kwargs['team'] ) & Q(userName = request.user ))
        dev=Role.objects.get(role="Developer")
        if member.role == dev:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def userIsTester(function):
    def wrap(request, *args, **kwargs):
        member = TeamMember.objects.get(Q(teamName = kwargs['team'] ) & Q(userName = request.user ))
        tes=Role.objects.get(role="Tester")
        print("hi")
        if member.role == tes:
        	print("bye")
        	return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def userIsMember(function):
    def wrap(request, *args, **kwargs):
        member = TeamMember.objects.filter(Q(teamName = kwargs['team'] ) & Q(userName = request.user ))
        if member:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap