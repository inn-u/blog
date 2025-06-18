from django import template
from blog.models import Tag, Comment, Post
from django.db.models import Max
from django.templatetags.static import static

register = template.Library()


@register.filter
def display_name(user):
    if not user:
        return 'Author'

    first_name = getattr(user, 'first_name', '')
    username = getattr(user, 'username', '')
    email = getattr(user, 'email', '')

    if first_name:
        return first_name
    elif username:
        return username
    elif email:
        return email.split('@')[0]
    else:
        return 'Author'


@register.simple_tag
def get_recent_tags(limit=10):
    return (
        Tag.objects.annotate(latest_use=Max('posts__published_date'))
        .filter(latest_use__isnull=False)
        .order_by('-latest_use')[:limit]
    )


@register.simple_tag
def get_latest_comments():
    return Comment.objects.select_related('user', 'post').order_by('-creation_date')[:2]


@register.simple_tag
def get_related_posts(post, count=3):
    if not post.category:
        return Post.objects.none()
    return (
        Post.objects.filter(category=post.category)
        .exclude(id=post.id)
        .order_by('-published_date')[:count]
    )


@register.simple_tag
def post_image_or_placeholder(post):
    first_image = post.images.first()
    if first_image:
        return first_image.image.url
    return static('placeholders/photo_placeholder.png')
