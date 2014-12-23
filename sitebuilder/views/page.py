import re
from django.shortcuts import render
from . import get_page_or_404


def page(request, slug='index'):
    """Render the requested page if found"""
    slug = re.sub('/$', '', slug)
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    content = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', content)
