from django.conf.urls import url

from . import views

urlpatterns = [
    # /api/1/43/
    url(r'^(?P<id>\d+)/(?P<level>.+)/$', views.add_entry, name='add_entry'),
]
