from django.db import models



# Create your models here.

class MainCategory(models.Model):
   
    name = models.CharField(max_length = 100)
    def __str__(self) :
        return self.name
    
    

class Category(models.Model):
    main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE,related_name='category')
    
    name = models.CharField(max_length=100,blank=True)

    def __str__(self) :
        return self.name + "----" + self.main_category.name 
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategory')
    name = models.CharField(max_length=100,blank=True)
    def __str__(self) :
        return self.category.main_category.name + " " + self.category.name+" " + self.name


class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    category = models.ManyToManyField(SubCategory)
 