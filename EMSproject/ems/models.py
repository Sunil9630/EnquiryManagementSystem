from django.db import models

class AdminDataBase(models.Model):
    firstname = models.CharField(max_length=30,null=False)
    lastname  = models.CharField(max_length=50, null=True)
    email  = models.EmailField(max_length=50, null=False)
    contact  = models.IntegerField(null=False)
    password  = models.CharField(max_length=50, null=False)

    def _str_(self):
        return self.name
    
class UserDataBase(models.Model):
    firstname = models.CharField(max_length=30,null=False)
    lastname  = models.CharField(max_length=50, null=True)
    email  = models.EmailField(max_length=50, null=False)
    contact  = models.IntegerField(null=False)
    password  = models.CharField(max_length=50, null=False)

    def _str_(self):
        return self.name

class userDashboardDataBase(models.Model):
    query=models.CharField(max_length=300)