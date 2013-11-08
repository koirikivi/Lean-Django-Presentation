from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('kanban.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
