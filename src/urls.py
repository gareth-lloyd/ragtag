from django.conf.urls.defaults import *
from feeds import BlogPostsFeed
import settings
from django.contrib import admin
admin.autodiscover()

# patterns for contrib modules
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
)
# blog urls
urlpatterns += patterns('',
    (r'^', include('blog.urls')),
    (r'^media/', include('media.urls.photos')),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': {'posts' : BlogPostsFeed}}
    ),
)

