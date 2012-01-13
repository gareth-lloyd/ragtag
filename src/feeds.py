from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from basic.blog.models import Post, Category

class BlogPostsFeed(Feed):
    title = 'Ragtag'
    link = '/'
    description = 'Latest articles from ragtag.info'

    def items(self):
        return Post.objects.published()[:10]