from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length= 50)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    description = models.CharField(max_length=300,default="Blank here comes the Description")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
