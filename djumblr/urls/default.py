from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      (r'regular/', include('djumblr.urls.regular')),
                      (r'photo/', include('djumblr.urls.photo')),
                      (r'quote/', include('djumblr.urls.quote')),
                      (r'link/', include('djumblr.urls.link')),
                      (r'conversation/', include('djumblr.urls.conversation')),
                      (r'video/', include('djumblr.urls.video')),
                      (r'audio/', include('djumblr.urls.audio')),
)