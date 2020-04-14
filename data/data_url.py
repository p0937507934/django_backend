
from django.urls import path
from .views import Data_list


urlpatterns = [
    path("/data", Data_list),
]
