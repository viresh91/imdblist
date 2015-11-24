from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie.views import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api')),
]
