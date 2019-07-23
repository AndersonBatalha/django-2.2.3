from django.shortcuts import render

def calendario(request):
    template = "app/calendario.html"
    return render(request=request, template_name=template)