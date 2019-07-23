from django.shortcuts import render

def classificacao(request):
    template = "app/classificacao.html"
    return render(request=request, template_name=template)