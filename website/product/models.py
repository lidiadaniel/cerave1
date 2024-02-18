from django.db import models
from django import forms
# Create your models here.

class ComapanyInformation(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self) -> str:
      return self.name
   
class Category(models.Model):
   name  = models.CharField(max_length=100)
   

   def __str__(self) -> str:
      return self.name
   
   
class Product(models.Model):
   product_name = models.CharField(max_length=100)
   product_description = models.TextField()   
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   image = models.ImageField(null=True)
   price = models.FloatField(null=True)
   date = models.DateTimeField(auto_now_add=True, null=True)
   def __str__(self) -> str:
      return self.product_name



class aboutUS(models.Model):
   name = models.CharField(max_length = 100)
   description = models.TextField() 
   image = models.ImageField()
   def __str__(self) -> str:
      return self.name
   

class MyForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Comment=  forms.TextInput()