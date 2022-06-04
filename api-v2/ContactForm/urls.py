from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_contact_form_data, name='post-form'),
    path('config', views.get_config_data, name='config'),
]
