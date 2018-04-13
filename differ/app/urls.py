from django.conf.urls import url
import views

urlpatterns = [

    url(r'^v1/diff/(?P<pk>[0-9]+)/right/$', views.right),
    url(r'^v1/diff/(?P<pk>[0-9]+)/left/$', views.left),
    url(r'^v1/diff/(?P<pk>[0-9]+)/$', views.differ),
]
