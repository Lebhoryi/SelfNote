from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^note$',  views.content , name="note"),
    url(r'^create$', views.create, name='create'),
    url(r'^update$', views.update, name='update'),
    url(r'^delete$', views.delete, name='delete'),
]