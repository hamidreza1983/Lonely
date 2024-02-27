from django.db import models


class Workexperience(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='work', default = 'work.jpg')

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    percent = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Services(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   


    def __str__(self):
        return self.title
    

class Resume(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.TextField()
    location = models.TextField()
    year = models.IntegerField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   


    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    

