from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from api.viewsets import CarViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^api/', include(router.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
