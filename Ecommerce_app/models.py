from django.db import models

# Create your models here.

class card_data(models.Model):
    id = models.AutoField(primary_key=True)  
    product_name=models.TextField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.ImageField(upload_to='static/')
    size = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    product_price=models.TextField()
    product_link=models.TextField()


class user_regestration(models.Model):
    id = models.AutoField(primary_key=True)  
    user_name=models.TextField(null=True)
    user_email = models.TextField(null=True)
    user_mobile = models.CharField(max_length=100,null=True)
    user_address = models.CharField(max_length=100,null=True)
    user_password= models.CharField(max_length=100,null=True)
    reg_Date=models.DateField(null=True)
    product_name1=models.TextField(null=True)
    description1 = models.TextField(blank=True, null=True)
    category1 = models.CharField(max_length=100, blank=True, null=True)
    brand1 = models.CharField(max_length=100, blank=True, null=True)
    product_image1 = models.ImageField(upload_to='static/',null=True)
    size1 = models.CharField(max_length=20, blank=True, null=True)
    color1 = models.CharField(max_length=20, blank=True, null=True)
    product_price1=models.TextField(null=True)
    






   
    

    
    