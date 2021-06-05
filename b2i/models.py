from django.db import models


# Create your models here.

class Predict(models.Model):
    pre1 = models.CharField(max_length=50)
    pre2 = models.CharField(max_length=50)
    pre3 = models.CharField(max_length=50)
    pre4 = models.CharField(max_length=50)
    pre5 = models.CharField(max_length=50)


class uploadImg(models.Model):
    img = models.ImageField(upload_to="images/")
