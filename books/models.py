from django.db import models


class BookModel(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    pages = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    content = models.TextField()

    def __str__(self):
        return self.title
