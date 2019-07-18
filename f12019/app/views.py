from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    template = "app/index.html"
    return render(request=request, template_name=template)