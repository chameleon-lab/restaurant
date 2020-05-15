from django.db import models
import uuid
import os


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category_order = models.IntegerField()
    visible_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Dish(models.Model):

    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name_dishes)
    description = models.CharField(max_length=300, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


class Gallery(models.Model):
    def get_file_name_gallery(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name_gallery)
    description = models.CharField(max_length=300, null=True)
    visible_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Contacts(models.Model):
    address = models.CharField(max_length=300, null=False)
    phone = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)




class Schedule(models.Model):
    day = models.CharField(max_length=15, null=False)
    start = models.TimeField(null=False)
    end = models.TimeField(null=False)


class Banner(models.Model):
    title = models.CharField(max_length=50, null=True)
    slogan = models.CharField(max_length=50, null=True)
    words = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=300, null=True)

class About(models.Model):
    def get_file_name_about(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/about/', filename)

    text = models.CharField(max_length=1000, null=False)
    photo_1 = models.ImageField(upload_to=get_file_name_about)
    photo_2 = models.ImageField(upload_to=get_file_name_about)