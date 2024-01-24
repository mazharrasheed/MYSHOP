from django.db import models

from .category import Category

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    pro_des=models.CharField(max_length=250 ,default="")
    pro_price=models.IntegerField(default=0)
    pro_img=models.ImageField(upload_to="uploaded/products/")
    category=models.ForeignKey(to=Category,on_delete=models.RESTRICT,)

    def __str__(self):
        return self.product_name
    
    @staticmethod
    def get_all_produts():
        return Products.objects.all()
    @staticmethod
    def get_all_produts_by_categoryid(categoryID):
        if categoryID:
            return Products.objects.filter(category=categoryID)      
        else:
            return Products.objects.all()