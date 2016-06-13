from django.conf.urls import url
from . import views

app_name = 'MBF'
urlpatterns = [
    url(r'^$', views.dashboard, name='MBF-dashboard'),
    url(r'^create-account/$', views.create_user, name="create-account" )
]
