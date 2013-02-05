from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^$', 'main'),
    url(r'^find_tweets/$', 'find_tweets'),
    url(r'^find_tweets/find/$', 'find_tweets'),
    url(r'^my_tweets/$', 'my_tweets'),
    # url(r'^test_twitter/', include('test_twitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
