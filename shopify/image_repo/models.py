from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Repository(models.Model):
    class Meta:
        verbose_name_plural = "Repositories"

    imageName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url():
        return reverse('image_repo:image_list')

    def __str__(self):
        return self.imageName
