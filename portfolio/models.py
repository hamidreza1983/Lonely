from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio',default='default.png')
    title = models.CharField(max_length=90)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    price = models.IntegerField(default=0)
    project_date = models.DateTimeField(default=datetime.datetime.now())
    project_url= models.CharField(max_length=90)
    client = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title