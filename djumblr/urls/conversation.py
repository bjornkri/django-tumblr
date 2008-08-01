from django.conf.urls.defaults import *

from djumblr.models import Conversation

conversation_info_dict = {
    'queryset': Conversation.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
                      url(r'^$', 
                          'archive_index', conversation_info_dict, 
                          name='djumblr_conversation_archive_index'),
                      url(r'^(?P<year>\d{4})/$',
                          'archive_year', conversation_info_dict,
                          name='djumblr_conversation_archive_year'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                          'archive_month', conversation_info_dict,
                          name='djumblr_conversation_archive_month'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                          'archive_day', conversation_info_dict,
                          name='djumblr_conversation_archive_day'),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<id>\d+)/$',
                          'object_detail', conversation_info_dict,
                          name='djumblr_conversation_detail'),
)