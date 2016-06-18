from django.conf.urls import url
from . import views

app_name = 'MBF'
urlpatterns = [
    url(r'^$', views.dashboard, name='MBF-dashboard'),
    url(r'^create-account/$', views.create_user, name="create-account" ),
    url(r'^add-child/$', views.create_child, name="create-child" ),
    url(r'^update001/$', views.update_breast, name="update-breast" ),
    url(r'^update002/$', views.update_bottle, name="update-bottle" ),
    url(r'^update003/$', views.update_diaper, name="update-diaper" ),
    url(r'^update004/$', views.update_temperature, name="update-temperature" ),
    url(r'^update005/$', views.update_sleep, name="update-sleep" ),
    url(r'^update006/$', views.update_wake, name="update-wake" ),
]
