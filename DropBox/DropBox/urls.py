#from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from DropBox.views import *
from django.conf.urls import *
#from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', main_page),

    # Register
    (r'^register/$', registration),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^portal/', include('portal.urls', namespace="portal")),
    #(r'^$', 'portal.views.portal_main_page', name='portal_main_page'),
    #(r'^portal/$', include('portal.urls', namespace="portal", app_name="portal")),
    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),

    

)