from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add', views.add_inclusion, name = 'add_inclusion'),
    url(r'^edit/(\d+)$', views.edit_department, name='edit'),
    url(r'^unit/(\d+)$', views.allowance_detail_info, name='allowance_detail_info'),
    url(r'^', views.all_inclusion, name='all_inclusion'),
]