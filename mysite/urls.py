from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^search$', 'search.views.home', name='search'),
    url(r'^$', 'news.views.home', name = 'home'),
    url(r'^news_list/$','news.views.news_list', name = 'news_list'),
    url(r'^news_list/(?P<pk>[0-9]+)/$','news.views.news_detail', name = 'news_detail'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^cms/', include('cms.urls', namespace='cms')),
    # url(r'^search/', include('search.urls', namespace='search')),
    url(r'^admin/', include(admin.site.urls)),
)
