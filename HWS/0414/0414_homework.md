# 0414_homework



![0414_homework](C:/Users/SSAFY_youji/ssafy7/ssafy_mine/HWS/0414/0414_homework.PNG)



```python
from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=128)
    adress = models.CharField(max_length=128)
    delivery = models.BooleanField()

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.TextField
    image = models.CharField(max_length=255)
    price = models.IntegerField
    key = models.IntegerField
    stock = models.IntegerField
    category = models.IntegerField
    event = models.BooleanField
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

```

