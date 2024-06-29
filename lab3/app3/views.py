from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse("Current datetime is : %s" %now)

def four_hours_ahead(request):
    ahead = datetime.datetime.now()+ datetime.timedelta(hours = 4)
    return HttpResponse("After four hours time will be : %s" %ahead)

def four_hours_before(request):
    past = datetime.datetime.now()+ datetime.timedelta(hours = -4)
    return HttpResponse("Before four hours time was : %s" %past)