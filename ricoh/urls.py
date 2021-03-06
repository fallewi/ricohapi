from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views import PrinterLog

router = routers.DefaultRouter()
router.register('logs', PrinterLog)
urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'ricoh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
