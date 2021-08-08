from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse, JsonResponse
from .models import App, Parameter, ConfigRequest

# Create your views here.

def params(request, app_name):
    param_list = Parameter.objects.filter(app__name=app_name)
    params = {p.name:p.value for p in param_list}
    return JsonResponse(params)
