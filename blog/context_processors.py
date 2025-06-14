from .models import Post


def recent_posts(request):
    posts = Post.objects.order_by('-published_date')[:3]
    return {'recent_posts': posts}
