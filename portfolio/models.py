from django.db import models

class Tab(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=20)
    sector = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    url = models.URLField()
    image_url = models.CharField(max_length=255)
    description = models.TextField()
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
