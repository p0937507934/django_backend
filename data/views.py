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
from django.views.decorators.csrf import csrf_exempt
from .custom import CustomTokenAuthentication
from .models import Data
from .serializer import DataSerializer, DataCheckSerializer
import ast
# Create your views here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)


@swagger_auto_schema(method='GET', responses={200: DataCheckSerializer(many=True)})
@swagger_auto_schema(method='POST', request_body=DataCheckSerializer, responses={204: "No content", 401: "No content"})
@api_view(["POST", "GET"])
@authentication_classes([CustomTokenAuthentication, ])
@permission_classes([IsAuthenticated])
def Data_list(request):
    
    if request.method == "GET":
        data = Data.objects.all()
        serializer = DataSerializer(
            data, many=True, context={"request": request})
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == "POST":
        
        recv_data = request.POST
        img = request.FILES.get("img")

        from device.models import Device
        from django.contrib.auth.models import User

        _mutable = recv_data._mutable
        recv_data._mutable = True
        recv_data['img'] = img
        recv_data._mutable = _mutable

        # check receive data format
        checkSerializer = DataCheckSerializer(data=recv_data)
        checkSerializer.is_valid(raise_exception=True)

        _mutable = recv_data._mutable
        recv_data._mutable = True
        try:
            recv_data['device_id'] = Device.objects.get(serial=recv_data.get("device_serial")).pk     
        except: 
            raise exceptions.AuthenticationFailed(_('裝置不存在'))
        recv_data['user_id'] = User.objects.get(username=request.user).pk


        try:
            recv_data['wavelength']=list(map(float, recv_data['wavelength'][1:-2].split(',')))
            recv_data['intensity']=list(map(float, recv_data['intensity'][1:-2].split(',')))
            recv_data['reflectance']=list(map(float, recv_data['reflectance'][1:-2].split(',')))
            recv_data['absorbance']=list(map(float, recv_data['absorbance'][1:-2].split(',')))
        except:
            raise exceptions.AuthenticationFailed(_('光譜資料錯誤'))
        predict_result=callapi() ##待補
        
        recv_data['label']=predict_result["label"]
        recv_data['confidence']=predict_result["confidence"]
        
        recv_data._mutable = _mutable
        print(recv_data)
        saveDataSerializer = DataSerializer(data=recv_data)
        saveDataSerializer.is_valid(raise_exception=True)
        saveDataSerializer.save()
        return JsonResponse({'predict_result':predict_result}, safe=False, status=200)

def callapi():
    return {"label":0,"confidence":0.9}