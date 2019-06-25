from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

def allPageShowData(request):
    get_settings=get_object_or_404(SettingsModel,pk=1)
    return {'general_settings':get_settings}