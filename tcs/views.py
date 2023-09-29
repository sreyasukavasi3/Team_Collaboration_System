from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from .forms import *
from django.core.mail import EmailMultiAlternatives
from tcs.email import *
from django.shortcuts import redirect
from django.core import signing
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import *
import random

def index(request):
	if request.method == 'POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data
			username = user['username']
			password =  user['password']
			user = authenticate(username = username, password = password)
			if user:
				login(request, user)
				return redirect('home',username=username)
			else:
				return HttpResponse('Blocked')
		else:
			return HttpResponse('Blocked')
	else:
		if request.user.is_authenticated:
			return redirect('home',username=request.user.username)
		form=LoginForm()
	return render(request, 'index.html', {'form':form})

@login_required
def home(request,username):
	return render(request, 'home1.html', {})

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data
			username = user['username']
			email =  user['email']
			password =  user['password']
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				otp=random.randint(100000,999999)
				sendWelcome(email,otp)
				otp=signing.dumps(otp, key='sekrit')
				password=signing.dumps(password, key='sekrit')
				request.session['username']=username
				return redirect('otp',otp=otp,username=username, email=email, password=password)
			else:
				return render(request, 'register1.html', {'form' : form, 'error':"username/emailid already exists"})
	else:
		form = UserRegistrationForm()
	return render(request, 'register.html', {'form' : form})

def otpVerification(request,otp,username, email, password):
	if request.session.has_key('username'):
		if request.method == 'POST':
			otp=signing.loads(otp, key='sekrit')
			password=signing.loads(password, key='sekrit')
			form = OtpForm(request.POST)
			if form.is_valid():
				typedOtp=form.cleaned_data['otp']
				if int(typedOtp)==int(otp):
					User.objects.create_user(username, email, password)
					user = authenticate(username = username, password = password)
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					del request.session['username']
					return HttpResponse('OTP mismatch')
		else:
			form = OtpForm()
		return render(request, 'otp.html', {'form' : form})
	else:
		return HttpResponse('Blocked')
