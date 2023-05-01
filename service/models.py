from django.db import models

class Service(models.Model):
    service_name=models.CharField(max_length=50)
    service_number=models.CharField(max_length=50)
    service_text=models.TextField()
class Registration(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    contact=models.IntegerField(null=True)
    age=models.CharField(max_length=50,null=True)
    village=models.CharField(max_length=50,null=True)

   

    

