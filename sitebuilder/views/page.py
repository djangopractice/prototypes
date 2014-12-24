import json
import re
from django.template import Context
from django.shortcuts import render
from . import get_page_or_404


def page(request, slug='index'):
    """Render the requested page if found"""
    slug = re.sub('/$', '', slug)
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    if page._meta is not None:
        meta = page._meta.render(Context())
        extra_context = json.loads(meta)
        context.update(extra_context)
    return render(request, 'page.html', context)
