from django.conf.urls.defaults import *

from djumblr.models import Photo

photo_info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'pub_date',
}

photo_generic_dict = dict(photo_info_dict)
photo_generic_detail_dict = dict(photo_info_dict)
photo_generic_dict['template_name'] = 'djumblr/generic.html'
photo_generic_detail_dict['template_name'] = 'djumblr/generic_detail.html'

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', photo_info_dict, 
                          name='djumblr_photo_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', photo_info_dict,
                          name='djumblr_photo_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', photo_generic_dict,
                          name='djumblr_photo_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', photo_generic_dict,
                          name='djumblr_photo_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<object_id>\d+)/$',
                          'object_detail', photo_generic_detail_dict,
                          name='djumblr_photo_detail'),
)