
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from ermsapp.forms import *
from ermsapp.models import *
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.

def Interviewer_CV_Profile(request):

    return render(request,'interviewer/cv_profile.html')