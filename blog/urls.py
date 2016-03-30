from django.conf.urls import url
from . import views

from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^general.html/$', views.general, name='general'),
    url(r'^dcmain.html/$', views.dcmain, name='dcmain'),
    url(r'^dcmain.html/big_data.html/$', views.big_data, name='big_data'),
    url(r'^dcmain.html/Data_Architecture.html/$', views.Data_Architecture, name='Data_Architecture'),
    url(r'^dcmain.html/BI_MI.html/$', views.BI_MI, name='BI_MI'),
    url(r'^dcmain.html/Master_Data.html/$', views.Master_Data, name='Master_Data'),
    url(r'^dcmain.html/Data_Q.html/$', views.Data_Q, name='Data_Q'),
    url(r'^dcmain.html/Project_M.html/$', views.Project_M, name='Project_M'),
    url(r'^PSmain.html/$', views.PSmain, name='PSmain'),
    url(r'^PSmain.html/books.html/$', views.books, name='books'),
]
