"""graddygame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.track_list, name='base'),
    
    url( r'^genres/(?P<pk>\d+)/$', views.genre, name="genre"),
    url(r'^genres/$', views.genre_list, name='genre-list'),
    url(r'^add-genre/$', views.add_genre, name='add-genre'),
    url(r'^add-genre/(?P<pk>\d+)/$', views.add_genre, name='edit-genre'),
    
    url(r'^add-track/$', views.add_track, name='add-track'),
    url(r'^add-track/(?P<pk>\d+)/$', views.add_track, name='edit-track'),
    url(r'^tracks/$', views.track_list, name='track-list'),
    url( r'^tracks/(?P<pk>\d+)/$', views.track, name="track"),
    url(r'^search-track/$', views.search_track, name='search-track'),
]