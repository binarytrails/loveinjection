from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'level1.views.login', name='login'),
    url(r'^auth/$', 'level1.views.auth', name='auth'),
    url(r'^auth/(?P<username>[\w ,.?!%&()@$-_:;\"\\]+)/(?P<password>[\w ,.?!%&()@$-_:;\"\\]+)/$', 'level1.views.auth', name='auth'),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
