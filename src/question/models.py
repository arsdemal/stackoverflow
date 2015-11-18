from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    rate = models.IntegerField(default=0)
    
class Answer():
    questions = models.ForeignKey(Question)
    text = models.IntegerField(default="")

# Create your models here.
