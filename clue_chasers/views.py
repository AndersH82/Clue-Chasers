from django.shortcuts import render
from.models import Profile

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})