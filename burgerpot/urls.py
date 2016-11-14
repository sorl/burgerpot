from django.conf.urls import url
from django.contrib import admin
from bugs.views import report, bugs_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'report/$', report, name='report'),
    url(r'^$', bugs_list, name='bugs_list'),
]
