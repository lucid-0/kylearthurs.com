from django.db import models

class BlogCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)

class Blog(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(BlogCategory,
                                 db_index=True,
                                 on_delete=models.PROTECT)
    main_image = models.ImageField

class Collectable(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=1000)
    main_image = models.ImageField(max_length=32000)

class Book(models.Model):
    collectable_data = models.OneToOneField(
        Collectable,
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=100)

class System(models.Model):
    collectable_data = models.OneToOneField(
        Collectable,
        on_delete=models.CASCADE
    )
    manufacturer = models.CharField(max_length=100)

class Game(models.Model):
    collectable_data = models.OneToOneField(
        Collectable,
        on_delete=models.CASCADE
    )
    platform = models.ForeignKey(System, on_delete=models.PROTECT)

class Record(models.Model):
    collectable_data = models.OneToOneField(
        Collectable,
        on_delete=models.CASCADE
    )
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
