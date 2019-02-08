from django.shortcuts import render
# Create your views here.
from .models import jobs


def home(request):
    job = jobs.objects
    return render(request, 'job/home.html', {'jobs': job})
