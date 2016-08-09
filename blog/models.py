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

class PhotoQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Photoset(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    photosets = models.ManyToManyField(Photoset)

    objects = PhotoQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo Entry"
        verbose_name_plural = "Photo Entries"
        ordering = ["-created"]
