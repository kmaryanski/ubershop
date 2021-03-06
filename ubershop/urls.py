from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from eshop.views import EShopView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ubershop.views.home', name='home'),
    # url(r'^ubershop/', include('ubershop.foo.urls')),
    url(r'^home/$','core.views.home_page'),
    url(r'^eshop/(?P<id>\d+)/$', EShopView.show_item),
    url(r'^eshop/(?P<id>\d+)/get_pdf', EShopView.get_item_pdf),
    url(r'^eshop/kategorie/(?P<category>.+)/$', EShopView.items_list),
    url(r'^eshop/szukaj/(?P<term>.+)/$', EShopView.search_item),
    url(r'^eshop/nowe/$', EShopView.newest_items),
    url(r'^eshop/popoularne/$', EShopView.popular_items),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
