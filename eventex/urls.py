from django.conf.urls import url, include
from django.contrib import admin

from eventex.core import views as eventex_views

urlpatterns = [
    url(r'^$', eventex_views.home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', admin.site.urls),
]
