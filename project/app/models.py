from django.db import models

# Create your models here.
class CustomQuerySet(models.QuerySet):
    def published_or_not(self):
        return self.filter(is_published=True)

class Library(models.Model):
    book_name = models.CharField(max_length=128)
    is_published = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.book_name
    
    custom_object = CustomQuerySet.as_manager() # замена objects