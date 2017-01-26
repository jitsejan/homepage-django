# History
#
# 2016-07-.. Add Entry, Tag
# 2016-..-.. Add Website, Project
# 2016-08-09 Add Photo, Photoset

from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    description = MarkdownField(default="", blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class WebsiteQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Website(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    image = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = WebsiteQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("website_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Website Entry"
        verbose_name_plural = "Website Entries"
        ordering = ["-created"]

class ProjectQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    image = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = ProjectQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Project Entry"
        verbose_name_plural = "Project Entries"
        ordering = ["-created"]


class Photoset(models.Model):
    flickr_id = models.CharField(max_length=50, default='No id')
    secret = models.CharField(max_length=50, default='No secret')
    title = models.CharField(max_length=200, default='No title')
    description = models.CharField(max_length=300, default='No description')
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(auto_now_add=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photoset"
        verbose_name_plural = "Photosets"
        ordering = ["date_update"]

class Photo(models.Model):
    flickr_id = models.CharField(max_length=50, default='No id')
    title = models.CharField(max_length=200, default='No title')
    description = models.CharField(max_length=300, default='No description')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    date_taken = models.DateTimeField(auto_now_add=True, blank=True)
    url = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    photoset = models.ForeignKey('Photoset', null=False, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ["-created"]

class ImageFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    imagefile = models.ImageField(upload_to='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)
