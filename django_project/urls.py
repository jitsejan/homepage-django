from django.conf.urls import include, url
from django.contrib import admin
from django_markdown import flatpages
from django.contrib.flatpages import views

admin.autodiscover()
flatpages.register()

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('blog.urls')),
    #url(r'^about$', 'flatpage', {'url': '/about/'}, name='about_url'),
#    url(r'^pages/', include('django.contrib.flatpages.urls')),
]
