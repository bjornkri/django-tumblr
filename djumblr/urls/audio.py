from django.conf.urls.defaults import *

from djumblr.models import Audio

audio_info_dict = {
    'queryset': Audio.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', audio_info_dict, 
                          name='djumblr_audio_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', audio_info_dict,
                          name='djumblr_audio_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', audio_info_dict,
                          name='djumblr_audio_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', audio_info_dict,
                          name='djumblr_audio_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<id>\d+)/$',
                          'object_detail', audio_info_dict,
                          name='djumblr_audio_detail'),
)