from django.shortcuts import render


def index(request):
    """ Basic home view for html templates"""
    return render(request, 'registration/login.html')
