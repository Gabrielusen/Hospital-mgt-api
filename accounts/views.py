# from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    """
    signup class view
    """
    # form_class =
    template_name = 'signup.html'
    success_url = reverse_lazy('login.html')
