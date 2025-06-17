from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView

from .forms import CommentForm
from .models import Post, Tag, Category, Comment


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


class SinglePostView(DetailView):
    template_name = 'post-single.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.filter(parent__isnull=True).order_by(
            '-creation_date'
        )

        parent_id = self.request.GET.get('parent')
        if parent_id and parent_id.isdigit():
            parent_comment = self.object.comments.filter(id=parent_id).first()
            context['reply_to'] = parent_comment
        else:
            context['reply_to'] = None
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user

            parent_id = request.POST.get('parent_id')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id, post=self.object)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    comment.parent = None

            comment.save()
            return redirect(self.request.path)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


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
