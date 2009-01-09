from django.conf.urls.defaults import *

from djumblr.models import Video

video_info_dict = {
    'queryset': Video.objects.all(),
    'date_field': 'pub_date',
}

video_generic_dict = dict(video_info_dict)
video_generic_detail_dict = dict(video_info_dict)
video_generic_dict['template_name'] = 'djumblr/generic.html'
video_generic_detail_dict['template_name'] = 'djumblr/generic_detail.html'

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', video_info_dict, 
                          name='djumblr_video_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', video_info_dict,
                          name='djumblr_video_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', video_generic_dict,
                          name='djumblr_video_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', video_generic_dict,
                          name='djumblr_video_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<object_id>\d+)/$',
                          'object_detail', video_generic_detail_dict,
                          name='djumblr_video_detail'),
)