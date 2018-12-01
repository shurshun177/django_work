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
    url(r'^api/v0/versions/(?P<vers_id>\d+)/$',
        views.get_version,
        name='vers_id'
        ),
    url(
        r'^api/v0/version/update/$',
        views.update_version,
        name='update_verasion'
    ),
    url(r'^api/v0/measures/$',
        views.measures,
        name='measures'
        ),
    url(r'^api/v0/measures/get_one/$',
        views.get_measure,
        name='measure_id'
        ),
    url(
        r'^api/v0/measure/update/$',
        views.update_measure,
        name='update_measure'
    ),
    url(
        r'^api/v0/version/update_del/(?P<vers_id>\d+)/$',
        views.del_vers
    ),
    url(
        r'^api/v0/measure/update_del/(?P<measure_id>\d+)/$',
        views.del_measure
    )


]