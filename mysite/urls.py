from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^cms/', include('cms.urls', namespace='cms')),
    # url(r'^search/', include('search.urls', namespace='search')),
    url(r'^admin/', include(admin.site.urls)),
)
