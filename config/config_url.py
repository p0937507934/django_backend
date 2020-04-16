
from django.urls import path
from .views import Config_list


urlpatterns = [
    path("/config", Config_list),
]
