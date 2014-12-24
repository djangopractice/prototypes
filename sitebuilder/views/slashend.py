from django.http import HttpResponsePermanentRedirect


def slashend(request, slug=''):
    """Redirect to slug with trailing slash"""
    return HttpResponsePermanentRedirect('/' + slug + '/')
