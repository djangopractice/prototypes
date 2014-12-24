from django.conf.urls import url
from .views.page import page
from .views.slashend import slashend

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^(?P<slug>[\w./-]*[^/])$', slashend, name='slashend'),
    url(r'^$', page, name='homepage'),
)
