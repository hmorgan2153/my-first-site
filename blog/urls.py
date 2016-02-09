from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^general/$', views.general, name='general.html'),
]
