from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from earningscalls import views
from django.conf.urls import include

urlpatterns = format_suffix_patterns(patterns('earningscalls.views',
    url(r'^$', 'api_root'),
    url(r'^earningscalls/$',
        views.EarningsCallList.as_view(),
        name='earningscall-list'),
    url(r'^earningscalls/(?P<pk>[0-9]+)/$',
        views.EarningsCallDetail.as_view(),
        name='earningscall-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',    
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)