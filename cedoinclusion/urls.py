from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^ajax_add_depart/$', views.ajax_add_depart, name='ajax_add_depart'),
    url(r'^add/$', views.sedoallowance_create, name='add_inclusion'),
    # url(r'^add_computer/$', views.computer_add, name='computer_add'),
    # url(r'^add2/$', views.add_inclusion, name='add_inclusion'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteInclusion.as_view(), name='delete'),
    url(r'^units/$', views.allUnit, name='all_unit'),
    url(r'^edit/(\d+)/$', views.edit_department, name='edit'),
    url(r'^unit/(\d+)/$', views.allowance_detail_info, name='allowance_detail_info'),
    url(r'^$', views.all_inclusion, name='all_inclusion'),
]