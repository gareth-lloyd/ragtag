from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(), name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        views.PostDayArchiveView.as_view(), name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        views.PostMonthArchiveView.as_view(), name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$', views.PostYearArchiveView.as_view(),
        name='blog_archive_year'),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        views.CategoryPostsListView.as_view(), name='blog_category_detail'
    ),
    url (r'^categories/$', views.CategoryListView.as_view(),
        name='blog_category_list'
    ),
    url(r'^tags/(?P<slug>[-\w]+)/$', views.TagPostsListView.as_view(),
        name='blog_tag_detail'
    ),
    url(r'^$', views.PostListView.as_view(),
        name='blog_index'),
    url(r'^page/(?P<page>\d+)/$', views.PostListView.as_view(),
        name='blog_index_paginated'),
)
