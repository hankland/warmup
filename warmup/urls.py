from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^users/login$', 'login.views.log'),
    url('^users/add$', 'login.views.add'),
    url('^TESTAPI/resetFixture$', 'login.views.reset'),
    url('^TESTAPI/unitTests$', 'login.views.tests'),
    url('', 'login.views.index'),
    # Examples:
    # url(r'^$', 'warmup.views.home', name='home'),
    # url(r'^warmup/', include('warmup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
