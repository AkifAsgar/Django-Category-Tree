from django.db import models



# Create your models here.

class Category(models.Model):
    main_category = models.ForeignKey('self',on_delete=models.CASCADE,related_name='category',null=True,blank=True)
    
    name = models.CharField(max_length=100,blank=True)

    def __str__(self) :
        return self.name  


class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    category = models.ManyToManyField(Category)
