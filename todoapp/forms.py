from django import forms
from todoapp.models import Todos,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=[
            'profile_pic',
            'date_of_field',
            'phone_no'
        ]
        widgets={
            'date_of_field':forms.DateInput(attrs={"class":"form_control","type":"date"})
        }









class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class TodoUpdateForm(forms.ModelForm):
    options=(
        (True,True),
        (False,False)
    )
    completed_status=forms.ChoiceField(choices=options)
    class Meta:
        model=Todos
        fields=[
            'task_name',
            'completed_status',
        ]







class TodoForm(forms.ModelForm):



    # task_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # user=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))form-control
    # date=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    # options=(
    #     (True,True),
    #     (False,False)
    # status=forms.ChoiceField(choices=options)
    class Meta():
        model=Todos
        fields=[
            "task_name",

                ]