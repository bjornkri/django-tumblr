from django.conf.urls.defaults import *

from djumblr.models import Photo

photo_info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', photo_info_dict, 
                          name='djumblr_photo_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', photo_info_dict,
                          name='djumblr_photo_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', photo_info_dict,
                          name='djumblr_photo_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', photo_info_dict,
                          name='djumblr_photo_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<id>\d+)/$',
                          'object_detail', photo_info_dict,
                          name='djumblr_photo_detail'),
)