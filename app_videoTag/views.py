from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from itertools import chain
from datetime import datetime
from mimetypes import guess_type
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.context_processors import auth
from django.db import transaction
from django.template import RequestContext
from django.shortcuts import render_to_response
from app_videoTag.models import *
from forms import *
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
from django.core.mail import send_mail
from urlparse import urlparse
from django.core.files import File
import urllib2
import re
import time
import json
import json as simplejson

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.db import transaction

# for fb login
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from config import CONFIG
authomatic = Authomatic(CONFIG, 'a super secret random string')



def home(request):
    context={}
    if request.method=="GET":
        documents = Document.objects.all().order_by('-created')
        context={'documents':documents}
        return render(request, "index.html", context)
    
    else: # for new facebook login user 
        new_user = User.objects.create_user(username=request.POST['username'],
                                         password=request.POST['password1'],
                                         email=request.POST['email'])
        new_user.is_active = True
        new_user.save()
        new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
        profile=Profile(user=new_user)
        profile.save()
        login(request, new_user)
        documents = Document.objects.all()
        context={'documents':documents}
        return render(request, "index.html", context)
        


def display(request):
    context={}
    return render(request, "page-elements.html", context)    

# fb login
def fblogin(request, provider_name):
    # We we need the response object for the adapter.
    response = HttpResponse()
    context={}
    # Start the login procedure.
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
     
    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
    if result:
        # If there is result, the login procedure is over and we can write to response.
        #response.write('<a href="..">Home</a>')
        
        if result.error:
            # Login procedure finished with an error.
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        
        elif result.user:

            # Hooray, we have the user!
            
            # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
            # We need to update the user to get more info.
            if not (result.user.name and result.user.id):
                 result.user.update()
            #Welcome the user.
            
            print result.user.name
            #print format(result.user.name)
            name = result.user.name.split()[0]
            #print name
            try:
                #name = result.user.name.split()[0]
                user = User.objects.get(username=name)
                print user.username
                print user.password
                print "here"
                user = authenticate(username=user.username)
                login(request, user)
                documents = Document.objects.all()
                context={'documents':documents}
                return render(request, "index.html", context)
            except User.DoesNotExist:
                print "None"
                context['username']=format(result.user.name)
                context['email'] = format(result.user.email)
                return render(request, "enter-password.html", context)  
            
    return response
    


    




