from django.conf.urls import url
from .views import post_list, post_detail, index, new_blog, latest_post_list

urlpatterns = [
    url(r'^home/$', index, name='home'),
    url(r'^paw_blog/$', post_list),
    url(r'^paw_blog/(?P<id>\d+)/$', post_detail),
    url(r'^newblogentry/$', new_blog, name='new_blog')
]