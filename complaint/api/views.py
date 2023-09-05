from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import serializers
from django.core.mail import send_mail


# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def create(self,request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Success'})
        return Response({'msg':'Failed'})
    
class SuperUserViewSet(viewsets.ViewSet):
    def create(self,request):
        ser = SuperUserSerializer(data=request.data)  
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Success'})
        return Response({'msg':'Failed'})
    
class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSer
    queryset=Question.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self,request):
        if self.request.user.is_superuser:
            raise serializers.ValidationError("method not allowded")
        else:
            ser = QuestionSer(data=request.data)
            if ser.is_valid():
                ser.save(user=request.user)    
                # send_mail('New Complaint','New Complaint','helloworld0007012@gmail.com',['helloworld0007012@gmail.com'])
                return Response(data=ser.data)
            return Response(data=ser.errors)
        
    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.user:
            object.delete()
            return Response(data="deleted")
        else:
            return Response(data="Not Possible")
    
    def update(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            raise serializers.ValidationError("method not allowded")
        else:
            partial = True # Here I change partial to True
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Question.objects.all()
        
        else:
            return Question.objects.filter(user=self.request.user)
           
    @action(methods=["POST"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        if self.request.user.is_superuser:
            user = request.user 
            id = kwargs.get('pk')
            question = Question.objects.get(id=id)
            ser = AnswerSer(data=request.data)
            if ser.is_valid():
                ser.save(user=user,question=question)
                # send_mail('Officials Reply','Your Complaint Status Received','helloworld000djangopython@gmail.com',['helloworld000djangopython@gmail.com'])
                return Response(data=ser.data)
            return Response(data=ser.errors)
        else:
            raise serializers.ValidationError("method not allowded")
   

class AnswerView(viewsets.ModelViewSet):
    serializer_class = AnswerSer
    queryset = Answer.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method not allowded")
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Answer.objects.filter(user=self.request.user)
        else:
           return serializers.ValidationError("permission denied for this user") 
    
    
    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.user:
            object.delete()
            return Response(data="deleted")
        else:
            return serializers.ValidationError("permission denied for this user")

        
    
class PoliceView(viewsets.ModelViewSet):
    serializer_class = PoliceSer
    queryset = Police.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.user:
            object.delete()
            return Response(data="deleted")
        else:
            return Response(data="Not Possible")
        
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Police.objects.filter(user=self.request.user)
        else:
           return serializers.ValidationError("permission denied for this user") 
        
    
    def create(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.user:
            ser = QuestionSer(data=request.data)
            if ser.is_valid():
                ser.save()  
                return Response(data=ser.data)
            return Response(data=ser.errors)

class QuestionViews(viewsets.ModelViewSet):
    serializer_class = QuestionSerr
    queryset=QuestionP.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self,request):
        if self.request.user.is_superuser:
            raise serializers.ValidationError("method not allowded")
        else:
            ser = QuestionSerr(data=request.data)
            if ser.is_valid():
                ser.save(user=request.user)
                # send_mail('New Complaint','New Complaint','helloworld0001997@gmail.com',['helloworld0001997@gmail.com'])
                return Response(data=ser.data)
            return Response(data=ser.errors)
        
    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.user:
            object.delete()
            return Response(data="deleted")
        else:
            return Response(data="Not Possible")
    
    def update(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            raise serializers.ValidationError("method not allowded")
        else:
            partial = True # Here I change partial to True
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        
    def get_queryset(self):
        if self.request.user.is_superuser:
            return QuestionP.objects.all()
        
        else:
            return QuestionP.objects.filter(user=self.request.user)
        
    @action(methods=["POST"],detail=True)
    def add_solution(self,request,*args,**kwargs):
        if self.request.user.is_superuser:
            user = request.user
            id = kwargs.get('pk')
            question = QuestionP.objects.get(id=id)
            ser = PoliceSer(data=request.data)
            if ser.is_valid():
                ser.save(user=user,question=question)
                # send_mail('Police Reply','Your Complaint Status Received','helloworld000djangopython@gmail.com',['helloworld000djangopython@gmail.com'])
                return Response(data=ser.data)
            return Response(data=ser.errors)
        else:
            raise serializers.ValidationError("method not allowded")
    

    
    
    
    
    

