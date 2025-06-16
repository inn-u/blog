from django.db.models import Count

from .models import Post, Category


def recent_posts(request):
    posts = Post.objects.annotate(comment_count=Count('comments')).order_by(
        '-published_date'
    )[:3]
    return {'recent_posts': posts}


def category_menu(request):
    categories = Category.objects.all()
    return {'category_menu': categories}
