from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=200)
  parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name


class MyItem(models.Model):
  name = models.CharField(max_length=200)
  category = models.ManyToManyField(Category)
  img = models.CharField(max_length=200, blank=True)
  description = models.TextField(blank=True)
  price = models.IntegerField(default=0)
  part_num = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return self.name + " " + self.part_num
