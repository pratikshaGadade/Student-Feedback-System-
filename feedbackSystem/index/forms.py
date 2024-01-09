from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback
from django import forms
class SignupForm(UserCreationForm):
      class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class FeedbackEntry(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'feedback']

