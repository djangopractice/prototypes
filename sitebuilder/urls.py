from django.conf.urls import url
from .views.page import page

urlpatterns = {
    url(r'^(?P<slug>[\w./-]+)$', page, name='page'),
    url(r'^$', page, name='homepage'),
}
