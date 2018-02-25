from django.conf.urls import url

from .views import APIKeyList, APIKeyCreate, APIKeyDelete

urlpatterns = [
    url(r'^list/$', APIKeyList.as_view()),
    url(r'^create/$', APIKeyCreate.as_view()),
    url(r'^delete/(?P<id>[0-9a-f-]+)/$', APIKeyDelete.as_view()),

]
