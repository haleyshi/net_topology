from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topo/', views.topo, name='topo'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILES_ROOT}),
]
