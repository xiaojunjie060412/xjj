from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Answer(models.Model):
    choice = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    relation = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice


class MyUser(User):

    telephone = models.CharField(max_length=11)
