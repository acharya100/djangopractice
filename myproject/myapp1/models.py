from django.db import models

# Create your models here.

class Department(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
        return self.name


class Individual(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height=models.DecimalField(decimal_places=2,max_digits=20,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images",null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name 

