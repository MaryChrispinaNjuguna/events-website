from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

def index (request):
    return render (request, 'index.html')