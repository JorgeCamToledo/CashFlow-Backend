from multiprocessing import context
from venv import create
from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Create your views here.

class LoginAuth(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,context = {'request':request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user = user)
        
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email': user.email
        })

       
