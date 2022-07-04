from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField
from image_check.settings import MEDIA_ROOT
# Create your models here
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])
class Pictures(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    def __str__(self) -> str:
        return self.name