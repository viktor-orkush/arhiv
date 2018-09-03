from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add', views.add_inclusion, name = 'add_inclusion'),
    url(r'all', views.all_inclusion, name='all_inclusion'),
    url(r'^', views.all_inclusion, name='all_inclusion'),
]