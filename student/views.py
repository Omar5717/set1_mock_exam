from django.shortcuts import render
from student.serializers import UserSerializer,StudentSerializer
from student.models import Students
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# class SignUpView(CreateAPIView):
#     serializer_class=UserSerializer

# class UserCreateView(CreateAPIView,ListAPIView):
#     serializer_class=StudentSerializer
#     queryset=Students.objects.all()

# class StudentView(RetrieveAPIView,UpdateAPIView):
#     serializer_class=StudentSerializer
#     queryset=Students.objects.all()

# class DeleteView(DestroyAPIView):
#     serializer_class=StudentSerializer


class SignupViewSet(ViewSet):
    def create(self,request):
        dser=UserSerializer(data=request.data)
        if dser.is_valid():
            User.objects.create_user(**dser.validated_data)
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentView(ModelViewSet):
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Students.objects.all()



    

