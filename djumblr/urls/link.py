from django.conf.urls.defaults import *

from djumblr.models import Quote

quote_info_dict = {
    'queryset': Quote.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', quote_info_dict, 
                          name='djumblr_quote_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', quote_info_dict,
                          name='djumblr_quote_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', quote_info_dict,
                          name='djumblr_quote_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', quote_info_dict,
                          name='djumblr_quote_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<id>\d+)/$',
                          'object_detail', quote_info_dict,
                          name='djumblr_quote_detail'),
)