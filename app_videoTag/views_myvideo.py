from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.context_processors import auth
from django.db import transaction
from django.template import RequestContext
from django.shortcuts import render_to_response
from app_videoTag.models import *
from django.db.models import Q
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.db import transaction


@login_required
def myvideo(request):
    context={}
    documents = Document.objects.filter(user=request.user)order_by('-created')
    context={'documents':documents}
    return render(request, "myvideo.html", context)
        
