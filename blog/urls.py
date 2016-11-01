# History
#
# 2016-08-09 Add photos_url

from django.views.generic import RedirectView
from django.conf.urls import include, url
from . import views, feed

urlpatterns = [
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^websites', views.WebsiteIndex.as_view(), name="websites_url"),
    url(r'^projects', views.ProjectIndex.as_view(), name="projects_url"),
    url(r'^photos', views.PhotoIndex.as_view(), name="photos_url"),
    url(r'^graphs', views.Graph.as_view(), name="graph"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^$', views.BlogIndex.as_view(), name="home_url"),
]
