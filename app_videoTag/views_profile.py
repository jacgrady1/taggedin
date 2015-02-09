from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

from mimetypes import guess_type

from models import *
from forms import *
import os
import time

from django.shortcuts import render, redirect, get_object_or_404


def profile(request,id):

  
    owner = get_object_or_404(User, id = id)
    profile = get_object_or_404(Profile, user=owner)
    form = ProfileForm(instance=profile)
    video = Document.objects.filter(user=request.user) 

    context = {'profile' : profile, 'owner': owner, 'form':form, 'video':video}
    return render(request, 'profile.html', context)
    

def getProfilePhoto(request, id):
    user=get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=user)
    
    if not profile.picture:
        raise Http404

    content_type = guess_type(profile.picture.name)
    return HttpResponse(profile.picture, content_type=content_type)

def edit(request):

    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "GET":
        form = ProfileForm(instance=profile)
        context = {'form' : form}
        return render(request, 'editprofile.html', context)
       
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if not form.is_valid():
        context = {'form' : form}
        return render(request, 'editprofile.html', context)
   
    form.save()
    
    profile = get_object_or_404(Profile, user=request.user)

    context = {'profile' : profile, 'owner': request.user, 'form':form}

    return render(request, 'profile.html', context)


    