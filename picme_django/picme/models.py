from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    category = models.ManyToManyField(
        Category, related_name="image_list", blank=True)
    title = models.CharField(max_length=50, default='no image title')
    img = models.FileField()

    def __str__(self):
        return self.title
