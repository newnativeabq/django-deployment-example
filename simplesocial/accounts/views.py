from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

# Create your views here.
class SignUpView(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'