from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question,Answer,Police,QuestionP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','password','email']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','password','email']
        
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    
        
class AnswerSer(serializers.ModelSerializer):
    user     = serializers.CharField(read_only=True)
    question = serializers.CharField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
        
      
class PoliceSer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = ['reply']

        
class QuestionSer(serializers.ModelSerializer):
    user     = serializers.CharField(read_only=True)
    date     = serializers.CharField(read_only=True)
    question_answers=PoliceSer(read_only=True,many=True)
   
    class Meta:
        model = Question
        fields = '__all__'
        

class QuestionSerr(serializers.ModelSerializer):
    user     = serializers.CharField(read_only=True)
    date     = serializers.CharField(read_only=True)
    police_answers=PoliceSer(read_only=True,many=True)
    
    class Meta:
        model = QuestionP
        fields = '__all__'
        
    
   
    
