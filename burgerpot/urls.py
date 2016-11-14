from django.conf.urls import url
from django.contrib import admin
from bugs.views import report, bug_list, bug_detail


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'report/$', report, name='report'),
    url(r'report/(?P<bug_id>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^$', bug_list, name='bugs_list'),
]
