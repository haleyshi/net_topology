from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def topo(request):
    context = {}

    if 'src' in request.GET:
        context["src"] = request.GET['src']

    return render(request, 'topo.html', context)

def raphael(request):
    context = {}
    return render(request, 'raphael-min.js', context)

def jquery(request):
    context = {}
    return render(request, 'jquery.min.js', context)
