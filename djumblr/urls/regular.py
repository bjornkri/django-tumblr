from django.conf.urls.defaults import *

from djumblr.models import Regular

regular_info_dict = {
    'queryset': Regular.objects.all(),
    'date_field': 'pub_date',
}

regular_generic_dict = dict(regular_info_dict)
regular_generic_detail_dict = dict(regular_info_dict)
regular_generic_dict['template_name'] = 'djumblr/generic.html'
regular_generic_detail_dict['template_name'] = 'djumblr/generic_detail.html'

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', regular_info_dict, 
                          name='djumblr_regular_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', regular_info_dict,
                          name='djumblr_regular_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', regular_generic_dict,
                          name='djumblr_regular_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', regular_generic_dict,
                          name='djumblr_regular_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<object_id>\d+)/$',
                          'object_detail', regular_generic_detail_dict,
                          name='djumblr_regular_detail'),
)