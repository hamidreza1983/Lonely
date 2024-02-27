from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.TextField()
    description_text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio", default="portfolio.jpg")
    project_date = models.DateTimeField(default=datetime.datetime.now())
    project_url = models.CharField(default="www.example.com")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.title
