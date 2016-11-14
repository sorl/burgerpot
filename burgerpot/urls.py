from django.conf.urls import url
from django.contrib import admin
from bugs.views import report, bug_list, bug_detail


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[-\w]+)/report/$', report, name='report'),
    url(r'^(?P<slug>[-\w]+)/report/(?P<bug_id>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^(?P<slug>[-\w]+)/$', bug_list, name='bug_list'),
]
