from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^your_profile/$', views.your_profile, name='user_profile'),

]

