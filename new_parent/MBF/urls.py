from django.conf.urls import url
from . import views

app_name = 'MBF'
urlpatterns = [
    url(r'^$', views.dashboard, name='MBF-dashboard'),
    url(r'^create-account/$', views.create_user, name="create-account" ),
    url(r'^add-child/$', views.create_child, name="create-child" ),
    url(r'^add-event/(?P<event_type>[a-z]+)/$', views.add_event, name="add-event" ),
]
