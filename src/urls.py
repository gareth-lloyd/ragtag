from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
from feeds import BlogPostsFeed
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
    (r'^photos/', include('media.urls.photos')),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': {'posts' : BlogPostsFeed}}
    ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
