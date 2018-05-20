from django.conf.urls import url
from .views import dog_list, dog_entry
from django.views.static import serve
from FPC.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^dogentries/$', dog_list),
    # url(r'^dogentries/(?P<id>\d+)/$', dog_detail),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^newdogentry/$', dog_entry, name="new_dogentry"),
]