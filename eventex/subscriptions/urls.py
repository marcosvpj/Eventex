import django.conf.urls

from eventex.subscriptions.views import new, detail


urlpatterns = [
    django.conf.urls.url(r'^$', new, name='new'),
    django.conf.urls.url(r'^(\d+)/$', detail, name='detail'),
]

