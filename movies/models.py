from django.db import models

# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=200)
    released_on=models.DateField()
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)

    def __str__(self):
        return self.title