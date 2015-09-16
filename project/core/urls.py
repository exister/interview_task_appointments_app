from django.conf.urls import patterns, url


urlpatterns_pages = patterns('core.views.pages',
    url('^$', 'index_page', name='index_page'),
)

urlpatterns_ajax = patterns('core.views.ajax',
    url('^doctors/$', 'doctors_list', name='doctors_list'),
    url('^dates/$', 'dates_list', name='dates_list'),
    url('^times/$', 'times_list', name='times_list'),
)


urlpatterns = patterns('',)
urlpatterns += urlpatterns_pages
urlpatterns += urlpatterns_ajax
