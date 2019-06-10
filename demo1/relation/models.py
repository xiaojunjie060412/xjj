from django.db import models

# Create your models here.


class Host(models.Model):
    name = models.CharField(max_length=20)


class App(models.Model):
    name = models.CharField(max_length=20)
    h = models.ManyToManyField(Host)


class MyManager(models.Manager):
    def first_info(self):
        return self.first()


class Info(models.Model):
    name = models.CharField(max_length=20)
    objects = MyManager()


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
