from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from .models import Config
from .serializer import ConfigSeriallizer
# Create your views here.
from data.custom import CustomTokenAuthentication


@swagger_auto_schema(method='GET', responses={200: ConfigSeriallizer(many=True)})
@swagger_auto_schema(method='POST', request_body=ConfigSeriallizer, responses={200: ConfigSeriallizer, 400: ConfigSeriallizer})
@api_view(["POST", "GET"])
@authentication_classes([CustomTokenAuthentication, ])
@permission_classes([IsAuthenticated])
def Config_list(request):
    if request.method == "GET":
        data = Config.objects.all()
        serializer = ConfigSeriallizer(
            data, many=True, context={"request": request})
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        data = request.POST
        # img = request.FILES.get("img_path")

        # _mutable = data._mutable
        # data._mutable = True
        # data['img_path'] = img
        # data._mutable = _mutable

        serializer = ConfigSeriallizer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse(status=204)
        
