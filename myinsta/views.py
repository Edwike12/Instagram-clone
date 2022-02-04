from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',)
