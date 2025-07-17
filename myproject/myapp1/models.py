from django.db import models

# Create your models here.

class Department(models.Model):
     name = models.CharField(max_length=100)


class Individual(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="images",null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name 

