from django.conf.urls import url
from . import views

app_name = 'MBF'
urlpatterns = [
    url(r'^$', views.dashboard, name='MBF-dashboard'),
    url(r'^home/$', views.home, name='MBF-home'),
    url(r'^create-account/$', views.create_user, name="create-account" ),
    url(r'^add-child/$', views.create_child, name="create-child" ),
    url(r'^add-caretaker/$', views.create_caretaker, name="create-caretaker" ),
    url(r'^add-event/(?P<event_type>[a-z]+)$', views.add_event, name="add-event" ),
    ## FIXME: Abstract out charts per event type
    url(r'^bottle-chart$', views.bottle_chart, name="bottle-chart" ),
    url(r'^temp-chart$', views.temperature_chart, name="temp-chart" ),
]
