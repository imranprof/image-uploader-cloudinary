from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(storage=MediaCloudinaryStorage(), upload_to='test_project/')  
    
    def __str__(self):
        return self.title
