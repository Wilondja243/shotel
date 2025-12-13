from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView


from shotel.app.user.models import User
from shotel.api.user.serializers import LoginSerializer, UserSerializer

class UserApiView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token, create = Token.objects.get_or_create(user=user)

            return Response(
                {
                    'success_message': 'User created successfully',
                    'token': token.key,
                    'object': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                    }
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            identifier = request.data.get('identifier')
            password = request.data.get('password')

            user = authenticate(request, username=identifier, password=password)

            if user is not None:
                token, create = Token.objects.get_or_create(user=user)

                return Response(
                    {
                        'success_message': 'User connected successfully',
                        'token': token.key,
                        'object':{
                            "id": user.id,
                            "username": user.username,
                        },
                        
                    },
                    status=status.HTTP_202_ACCEPTED
                )
            else:
                messages.error(request, "Incorrect user infos")
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
            

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
