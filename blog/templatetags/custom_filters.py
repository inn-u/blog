from django import template
from blog.models import Tag
from django.db.models import Max

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
