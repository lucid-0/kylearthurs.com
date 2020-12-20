from django.db import models


class BlogCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(BlogCategory,
                                 db_index=True,
                                 on_delete=models.PROTECT)
    main_image = models.ImageField


class Book(models.Model):
    title = models.CharField(max_length=100, db_index=True, default="Book")
    description = models.CharField(max_length=1000, null=True)
    main_image = models.ImageField(max_length=32000, null=True)
    original_release = models.DateField(null=True)
    author = models.CharField(max_length=100, null=True)


class System(models.Model):
    title = models.CharField(max_length=100, db_index=True, default="System")
    description = models.CharField(max_length=1000, null=True)
    main_image = models.ImageField(max_length=32000, null=True)
    original_release = models.DateField(null=True)
    manufacturer = models.CharField(max_length=100)


class Game(models.Model):
    title = models.CharField(max_length=100, db_index=True, default="Game")
    description = models.CharField(max_length=1000, null=True)
    main_image = models.ImageField(max_length=32000, null=True)
    original_release = models.DateField(null=True)
    platform = models.ForeignKey(System, on_delete=models.PROTECT)


class Record(models.Model):
    title = models.CharField(max_length=100, db_index=True, default="Vinyl Record")
    description = models.CharField(max_length=1000, null=True)
    main_image = models.ImageField(max_length=32000, null=True)
    original_release = models.DateField(null=True)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
