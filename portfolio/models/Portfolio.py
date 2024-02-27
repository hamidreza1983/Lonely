from django.db import models
import datetime
from .Category import Category
from .Client import Client


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio", default="portfolio.jpg")
    project_date = models.DateTimeField(default=datetime.datetime.now())
    project_url = models.CharField(max_length=100,default="www.example.com")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.title
