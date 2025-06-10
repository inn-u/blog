from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


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


class ContactPage(TemplateView):
    template_name = 'contact.html'


class Error404(TemplateView):
    template_name = '404.html'
