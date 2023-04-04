from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    donate = models.FloatField(default=0)
    category = models.ManyToManyField(Category)