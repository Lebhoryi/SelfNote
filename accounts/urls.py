from django.conf.urls import url
from django.contrib.auth import views as user_view

urlpatterns = [
    url(r'^login/$', user_view.login, name='login'),
    url(r'^logout/$', user_view.logout, name='logout'),
]