from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from forms import *

def testSingle(request):
    return render(request,"testSingleController.html",{})

def refresh_video(request):
    url =request.POST['url']
    #print request.POST['url']
    #url = form.cleaned_data['url']
    url = Url(url=url)
    url.save()
    suffix="?api=1&title=0&amp;byline=0&amp;portrait=0" 
    urlwithsuffix=url.url+suffix
    return render_to_response('video-appended.html',
                          {'url': urlwithsuffix},
                          context_instance=RequestContext(request))


def testVideoTag(request):
    return render(request,"TestNewVideoTag.html",{})


def danmu(request):
    return render(request,"danmu.html",{})
 