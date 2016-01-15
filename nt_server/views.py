from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from nt_server.command_runner import *

# Create your views here.
def index(request):
  return HttpResponse('Hello')

def json(request):
  topo = getAll()
  return JsonResponse(topo, safe=False)

