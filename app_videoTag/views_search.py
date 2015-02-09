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
from django.db.models import Q

def search(request):

    keywords=request.GET.get('searchwords')

    documents = Document.objects.filter(Q(text__icontains=keywords) | Q(description__icontains=keywords)).order_by('-created')
    
    context = {'documents' : documents }
    return render(request, 'index.html', context)


    