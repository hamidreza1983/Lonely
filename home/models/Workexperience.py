from django.db import models

class Workexperience(models.Model):
    image = models.ImageField(upload_to="work", default="work.jpg")

