from django.urls import re_path
from . import consumers

'''
    Route Configs for websocket vote request
'''
websocket_urlpatterns = [
    re_path(r'ws/polls/(?P<poll_uid>[^/.]+)/$',
        consumers.PollVoteConsumer)
]