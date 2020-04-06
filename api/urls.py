from django.urls import re_path, include
from rest_framework import routers
from . import viewsets as vs 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.SimpleRouter()
router.register(r'polls', vs.PollViewSet, basename='polls')
router.register(r'polls/(?P<pk>[^/.]+)/candidates', vs.PollCandidateViewSet, basename='poll-candidates')
router.register(r'candidates', vs.CandidateViewSet, basename='candidates')

urlpatterns = [
     re_path(r'^token/access/$', TokenObtainPairView.as_view(), name='access-token'),
     re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='refresh-token'),
     re_path(r'^polls/create/$', views.create_poll, name='create-poll'),
     re_path(r'^', include(router.urls)),
]
