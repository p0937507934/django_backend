from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from .models import Data
from django.http import HttpResponse, JsonResponse
from .serializer import DataSerializer
from rest_framework.parsers import JSONParser, MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from .custom import CustomTokenAuthentication
# Create your views here.



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)





@api_view(["POST", "GET"])
@authentication_classes([CustomTokenAuthentication, ])
@permission_classes([IsAuthenticated])
def Data_list(request):

    if request.method == "GET":

        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == "POST":

        data = request.POST
        img = request.FILES.get("img_path")

        _mutable = data._mutable
        data._mutable = True
        data['img_path'] = img
        data._mutable = _mutable

        serializer = DataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
