from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title       = models.CharField(max_length=100)
    complaint   = models.CharField(max_length=500)
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='image',null=True)
    date        = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def question_answers(self):
        return self.answer_set.all()
    
    
class QuestionP(models.Model):
    title       = models.CharField(max_length=100)
    complaint   = models.CharField(max_length=500)
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='images',null=True)
    date        = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def police_answers(self):
        return self.police_set.all()
    

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    reply    = models.CharField(max_length=500)
    
    
class Police(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionP,on_delete=models.CASCADE)
    reply    = models.CharField(max_length=500)
    
    
    
