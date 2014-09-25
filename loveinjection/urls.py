from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sqlite3app.views.level1', name='home'),
    url(r'^sqlite3/$', 'sqlite3app.views.level1', name='sqlite3-level1'),
    url(r'^sqlite3/level1/$', 'sqlite3app.views.level1', name='sqlite3-level1'),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
