from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import dates
from django.conf import settings

from blog.models import Post, Category
from tagging.models import Tag, TaggedItem

class PostListView(ListView):
    queryset=Post.objects.published()
    paginate_by=getattr(settings,'BLOG_PAGESIZE', 20)

class PostYearArchiveView(dates.YearArchiveView):
    queryset=Post.objects.published()
    date_field='publish'
    make_object_list=True

class PostMonthArchiveView(dates.MonthArchiveView):
    queryset=Post.objects.published()
    date_field='publish'
    make_object_list=True

class PostDayArchiveView(dates.DayArchiveView):
    queryset=Post.objects.published()
    date_field='publish'
    make_object_list=True

class PostDetailView(dates.DateDetailView):
    date_field='publish'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.published()

class CategoryListView(ListView):
    queryset=Category.objects.all()

class CategoryPostsListView(ListView):
    template_name = 'blog/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            CategoryPostsListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.category = get_object_or_404(Category, slug__iexact=slug)
        return self.category.post_set.published()

class TagPostsListView(ListView):
    template_name = 'blog/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            CategoryPostsListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.tag = get_object_or_404(Tag, name__iexact=slug)
        return TaggedItem.objects.get_by_model(Post,tag).filter(status=2)
