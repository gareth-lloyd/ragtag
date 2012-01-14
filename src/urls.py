from django.conf.urls.defaults import *
from basic.blog import views
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
    url(r'^$', view=views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view=views.post_detail,
        name='blog_detail'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$', view=views.category_detail,
        name='blog_category_detail'
    ),
    url(r'^categories/$', view=views.category_list, name='blog_category_list'),
    url(r'^tags/(?P<slug>[-\w]+)/$', view=views.tag_detail,
        name='blog_tag_detail'
    ),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': {'posts' : BlogPostsFeed}}
    ),
)

