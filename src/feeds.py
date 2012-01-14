from django.contrib.syndication.feeds import Feed
from basic.blog.models import Post

class BlogPostsFeed(Feed):
    title = 'Ragtag'
    link = '/'
    description = 'Latest articles from ragtag.info'

    def items(self):
        return Post.objects.published()[:10]
