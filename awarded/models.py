from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()
