from django.conf.urls import url
#from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1.0/versions/$',
        views.get_versions,
        name='versions'
        ),
    url(
        r'^api/v1.0/versions/(?P<vers_id>\d+)/$',
        views.get_version,
        name='vers_id'
    ),
    url(r'^api/v1.0/measures/$',
        views.get_measures,
        name='measures'
        ),
    url(r'^api/v1.0/measures/(?P<measure_id>\d+)/$',
        views.get_measure,
        name='measure_id'
        ),


]