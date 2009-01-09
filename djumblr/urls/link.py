from django.conf.urls.defaults import *

from djumblr.models import Link

link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

link_generic_dict = dict(link_info_dict)
link_generic_detail_dict = dict(link_info_dict)
link_generic_dict['template_name'] = 'djumblr/generic.html'
link_generic_detail_dict['template_name'] = 'djumblr/generic_detail.html'

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', link_info_dict, 
                          name='djumblr_link_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', link_info_dict,
                          name='djumblr_link_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', link_generic_dict,
                          name='djumblr_link_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', link_generic_dict,
                          name='djumblr_link_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<object_id>\d+)/$',
                          'object_detail', link_generic_detail_dict,
                          name='djumblr_link_detail'),
)