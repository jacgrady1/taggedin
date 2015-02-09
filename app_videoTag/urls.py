from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # home page     
    url(r'^$', 'app_videoTag.views.home',name='home'),
    # upload page 
    url(r'^upload$', 'app_videoTag.views_upload.upload',name='upload'),
    # play single video
    url(r'^play/(?P<id>\d+)$', 'app_videoTag.views_play.play',name='play'),

    # add tagging 
    url(r'^addtag/(?P<id>\d+)$', 'app_videoTag.views_play.addtag',name='addtag'),
    # gongxun display all element page for front end modification
    url(r'^display$', 'app_videoTag.views.display',name="display"),

    # gongxun - facebook login
    url(r'^login/(\w*)', 'app_videoTag.views.fblogin', name='fblogin'),
    # login/logout
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html'},name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login',name="logout"),
    
    # view_register
    url(r'^register$', 'app_videoTag.views_register.register', name='register'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'app_videoTag.views_register.confirm_registration', name='confirm'),
    
    url(r'^editprofile$', 'app_videoTag.views_profile.edit', name = 'editprofile'),
    url(r'^viewprofile/(?P<id>\d+)$', 'app_videoTag.views_profile.profile', name='viewprofile'),
    
    url(r'^photo/(?P<id>\d+)$', 'app_videoTag.views_profile.getProfilePhoto', name='photo'),
    url(r'^search$', 'app_videoTag.views_search.search', name = 'search'),
    


)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


