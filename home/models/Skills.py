from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=20)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return self.name