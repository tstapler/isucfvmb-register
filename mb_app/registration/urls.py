from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registered$', views.view_registered, name='view_registered'),
    url(r'^.*$', views.index, name='index'),
]
