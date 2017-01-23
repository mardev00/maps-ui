
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^map/(\w+)/$', views.mapview, name='mapview'),
    url(r'^$', views.index),
    url(r'^map', views.mapview),
    url(r'^post_url/$', views.post_map, name='post_map'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
