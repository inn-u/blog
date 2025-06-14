from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post, Tag, Category


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-published_date')[:8]

        featured_post = Post.objects.filter(is_featured=True).first()
        if not featured_post:
            featured_post = Post.objects.order_by('-published_date').first()

        context['featured_post'] = featured_post
        return context


class SingePostView(DetailView):
    template_name = 'post-single.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class AboutPage(TemplateView):
    template_name = 'about.html'


class ListPostView(ListView):
    template_name = 'post-list.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_queryset(self):
        queryset = super().get_queryset()

        # tag filter
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            self.tag = tag
            queryset = queryset.filter(tags=tag)

        # category filter
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            self.category = category
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'tag'):
            context['tag'] = self.tag
        return context


class ContactPage(TemplateView):
    template_name = 'contact.html'


class Error404(TemplateView):
    template_name = '404.html'
