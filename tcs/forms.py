from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class OtpForm(forms.Form):
    otp = forms.CharField(
        required = True,
        label = 'OTP',
        max_length = 6
    )
    
class LoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'username',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'password',
        max_length = 32,
        widget = forms.PasswordInput()
    )