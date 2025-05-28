from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post


class HomePageView(TemplateView):
    template_name = 'index.html'


class SingePostView(DetailView):
    template_name = 'post-single.html'
    model = Post
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"
