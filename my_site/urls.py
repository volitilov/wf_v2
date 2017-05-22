from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^info$', views.info, name='info'),
    url(r'^services$', views.services, name='services'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^feedback$', views.contacts, name='feedback'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.work, name='work'),
]
