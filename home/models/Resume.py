from django.db import models



class Resume(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    location = models.TextField()
    year = models.IntegerField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title