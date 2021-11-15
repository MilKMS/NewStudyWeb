from django import forms
from django.contrib.auth.hashers import check_password, make_password

from .models import Users


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Enter the Email.'
        },
        max_length=64, label='Email'
    )

    password = forms.CharField(
        error_messages={
            'required': 'Input Password'
        },
        widget=forms.PasswordInput, label='Password'
    )

    re_password = forms.CharField(
        error_messages={
            'required': 'Input Check-Password'
        },
        widget=forms.PasswordInput, label='Password Check'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('re_password', 'Password do not match')
            else:
                users = Users(
                    email=email,
                    password=make_password(password)
                )
                users.save()


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Enter the Email.'
        },
        max_length=64, label='Email'
    )

    password = forms.CharField(
        error_messages={
            'required': 'Input Password'
        },
        widget=forms.PasswordInput, label='Password'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                self.add_error('password', 'Dose Note Exist Email or Wrong Password')
                return

            if not check_password(password, user.password):
                self.add_error('password', 'Dose Note Exist Email or Wrong Password')
            else:
                self.email = user.email