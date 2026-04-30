from django.db import models

# Create your models here.
class student(models.Model):
    rollnum=models.CharField(max_length=100)
    name=models.CharField(max_length=300)
    age=models.IntegerField()
    email=models.EmailField()
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class teacher(models.Model):
    empid=models.CharField(max_length=100)
    name=models.CharField(max_length=300)
    email=models.EmailField()
    subject=models.CharField(max_length=100)

    def __str__(self):
        return self.name