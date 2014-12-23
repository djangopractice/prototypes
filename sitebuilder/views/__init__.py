import os
from django.conf import settings
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join


def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error"""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
    with open(file_path, 'r') as f:
        page = Template(f.read())
    return page
