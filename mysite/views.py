from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django_facebook.models import FacebookCustomUser
from django_facebook.api import FacebookUserConverter as fbconvert

from forms import SignupForm

def home(request):
    #me = FacebookCustomUser.objects.all()[0]
    #data = fbconvert.facebook_profile_data(me)
    #print(data)
    return render(request, "home/test.html")
    if "fb_id" in request.COOKIES.keys():
        fb_id = request.COOKIES["fb_id"]
        return render(request, "home/home.html", {'id': fb_id})
    return render(request, "home/first.html")

