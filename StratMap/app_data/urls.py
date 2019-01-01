from django.conf.urls import url
#from django.urls import path
from . import views

urlpatterns = [
    url(
        r'^api/v0/$',
        views.index,
        name='v'
    ),
    url(
        r'^api/v0/test/$',
        views.index_0
    ),
    url(r'^api/v0/versions/$',
        views.versions,
        name='versions'
        ),
    url(r'^api/v0/versions/(?P<vers_id>\S+)/$',
        views.get_version,
        name='vers_id'
        ),
    url(
        r'^api/v0/version/update/(?P<vers_id>\S+)/$',
        views.update_version,
        name='update_version'
    ),
    url(r'^api/v0/measures/$',
        views.measures,
        name='measures'
        ),
    url(r'^api/v0/measures/(?P<id>\S+)/$',
        views.get_measure,
        name='measure_id'
        ),
    url(
        r'^api/v0/measure/update/(?P<measure_id>\S+)/$',
        views.update_measure,
        name='update_measure'
    ),
    url(
        r'^api/v0/version/del_vers/(?P<vers_id>\S+)/$',
        views.del_vers
    ),
    url(
        r'^api/v0/measure/del_measure/(?P<measure_id>\S+)/$',
        views.del_measure
    ),
    url(
        r'^api/v0/available_measures/(?P<code>\d+)/(?P<topic>\d+)/$',
        views.available_measures
    ),
    url(
        r'^api/v0/tables/$',
        views.get_dec
    ),
    url(
        r'^api/v0/last_version/$',
        views.last_version
    ),

]