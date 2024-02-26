from django.db import models

# Create your models here.
class User_db(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)


    def __str__(self):
        return self.Name

class Password_db(models.Model):
    UserID = models.CharField(max_length=10 , default="")
    UserName = models.CharField(max_length=100 , default="")


    def __str__(self):
        return self.UserID + "--" + self.UserName