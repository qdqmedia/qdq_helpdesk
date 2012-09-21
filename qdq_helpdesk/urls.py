from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('helpdesk.urls')),
    # url(r'^$', 'qdq_helpdesk.views.home', name='home'),
    # url(r'^qdq_helpdesk/', include('qdq_helpdesk.foo.urls')),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
