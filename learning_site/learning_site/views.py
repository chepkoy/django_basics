from django.shortcuts import render


def welcome_home(request):
    return render(request,'home.html')

