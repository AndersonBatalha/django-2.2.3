from django.shortcuts import render

def equipes(request):
    template = "app/equipes.html"
    return render(request=request, template_name=template)