from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^(?P<star_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<star_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^(?P<star_id>[0-9]+)/comment/$', views.comment, name='comment'),
        url(r'^(?P<star_id>[0-9]+)/support/$', views.support, name='support'),
        ]
