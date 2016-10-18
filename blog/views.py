# History
#
# 2016-08-09 Add PhotoIndex

from django.shortcuts import render
from django.views import generic

from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 5

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class WebsiteIndex(generic.ListView):
    queryset = models.Website.objects.published()
    template_name = "website.html"

class ProjectIndex(generic.ListView):
    queryset = models.Project.objects.published()
    template_name = "project.html"

class PhotoIndex(generic.ListView):
    queryset = models.Photoset.objects.all()
    template_name = "photo.html"
