from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello kind user! Here's your poll index.")
# Create your views here.
