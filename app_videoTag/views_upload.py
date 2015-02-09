from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from models import Document
from forms import DocumentForm
import os
import time

@login_required
def upload(request):

    html= 'upload-video.html'

    video_to_add=Document(user=request.user)
    
    if request.method=='GET':
        documentForm=DocumentForm(instance=video_to_add)
        return render_to_response(
         html,
         {'form': documentForm},
         context_instance=RequestContext(request)
         )

    documentForm=DocumentForm(request.POST, request.FILES, instance=video_to_add)
    
    if not documentForm.is_valid():
        return render_to_response(
         html,
         {'form': documentForm},
         context_instance=RequestContext(request)
         )

    documentForm.save()

    return redirect('home')

    