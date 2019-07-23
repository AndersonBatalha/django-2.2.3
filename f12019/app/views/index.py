from django.shortcuts import render

def index(request):
    template = "app/index.html"
    return render(request=request, template_name=template)