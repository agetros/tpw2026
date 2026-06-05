import hashlib

from django import template

register = template.Library()


@register.filter
def category_badge(categories):
    if not categories:
        return '<span class="badge rounded-pill text-bg-secondary"><i class="bi bi-tags-fill"></i> Sin categorías</span>'
    badges = []
    for category in categories.split(","):
        badges.append(
            f'<span class="badge rounded-pill text-bg-secondary"><i class="bi bi-tags-fill"></i> {category.strip()}</span>'
        )
    return " ".join(badges)
