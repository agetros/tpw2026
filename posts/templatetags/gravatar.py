import hashlib

from django import template

register = template.Library()


@register.filter
def gravatar(email, size=80):
    if not email:
        return "https://www.gravatar.com/avatar/?d=mp"

    email_hash = hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()

    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=mp"
