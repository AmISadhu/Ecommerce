from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="pages_win")
def pages_win(value, _max):
    size = settings.COUNT_PAGES
    start = max(int(value) - (size // 2), 1)
    end = min((start + (size - 1)), int(_max))
    if (end - start + 1) < size:
        start = end - size + 1
    return range(start, end + 1)


@register.filter(name="add_tag")
def curr_add_tag_url(url, arg):
    if "?" in url:
        url += f"&tag={arg}"
    else:
        url += f"?tag={arg}"

    return url
