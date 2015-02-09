from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Document
from forms import *
from django.shortcuts import render, redirect

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
from django.db import transaction


from django.core import serializers
from django.template.loader import render_to_string
from django.templatetags.static import static
import time
from django.utils.encoding import smart_str
import sys
import os

def play(request,id):
    document = Document.objects.get(id=id)

    context={'document':document,'form':TaggingForm()}    
    return render(request,"danmu.html",context)

@login_required
# @transaction.atomic
def addtag(request,id):
    form = TaggingForm(request.POST)
    document = Document.objects.get(id=id)
    #print "url:",document.docfile.url
    if not form.is_valid(): 
        context={'document':document,'form':form}
        #print "invalid form"  
        return render(request,"danmu.html",context)
    
    startsecond = request.POST['startpoint']
    
    timeint=int(float(startsecond))
    starttime=time.strftime('%M:%S', time.gmtime(timeint))
    startsecond = str(timeint+1)
    
    tag = Tagging(user=request.user,
        starttime=starttime,
        startsecond=startsecond,
        text=form.cleaned_data['text'],
        video=document)
    
    tag.save()
    document.tagging_set.add(tag)
    
    context={'document':document,'form':form}
    tags=document.tagging_set.all()
    xml = render_to_string('file.xml', {'tags': tags})
    xml = smart_str(xml)
    projectpath=os.getcwd()
    filename=document.text+'-'+document.user.username+".xml" 
    filepath = os.path.join(projectpath,"app_videoTag/static/xml/"+filename)  
    outfile = open(filepath, "w")
    outfile.write(xml)
    outfile.close()
    data = serializers.serialize("json", [tag]) 
    return HttpResponse(data, content_type='application/json')
        

