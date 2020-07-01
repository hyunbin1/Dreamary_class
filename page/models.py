from django.db import models

# Create your models here.

class Designer(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    # admin 등록시 등록된 이름으로 나오게 하는 법
    
    def __str__(self):
        return self.name