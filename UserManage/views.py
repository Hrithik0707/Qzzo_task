from django.shortcuts import render,redirect
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
import jwt
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib import auth
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,LoginSerializer
from rest_framework.views import APIView

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='UserManage/register.html'

    def get(self,request):
        serializer = UserSerializer()
        return Response({'serializer':serializer})

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('login')


def profile(request,unique_id):
        user = User.objects.filter(unique_id=unique_id)
        print(user)
        return render(request,'UserManage/profile.html',{'user':user})




class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='UserManage/login.html'
    def get(self,request):
        serializer = LoginSerializer()
        return Response({'serializer':serializer})

    

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            email =data['email']
            password = data['password']
            user = auth.authenticate(username=email, password=password)
        
            if user:
                auth_token = jwt.encode(
                    {'unique_id': user.unique_id}, settings.JWT_SECRET_KEY)
                serializer = UserSerializer(user)
                data = serializer.data
                total = {'user': data, 'token': auth_token}
                print(data['unique_id'])
                return redirect('profile',unique_id=data['unique_id'])

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


