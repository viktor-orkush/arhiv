from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.sedoallowance_create, name='add_inclusion'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteInclusion.as_view(), name='delete'),
    url(r'^units/$', views.allUnit, name='all_unit'),
    url(r'^edit/([0-9]+)/$', views.sedo_allowance_edit, name='edit'),
    url(r'^unit/(\d+)/$', views.allowance_detail_info, name='allowance_detail_info'),
    url(r'^$', views.all_inclusion, name='all_inclusion'),
]