from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registered$', views.view_registered),
    url(r'^results$', views.return_data),
    url(r'^login$', views.login),
    url(r'^.*$', views.index),
]
