from django.shortcuts import render

def pilotos(request):
    template = "app/pilotos.html"
    return render(request=request, template_name=template)