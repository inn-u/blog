from django import template

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
