
from django.urls import path
from .views import Device_list


urlpatterns = [
    path("/device", Device_list),
]
