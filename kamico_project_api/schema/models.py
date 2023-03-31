from django.db import models

# Create your models here.
class PipesModels(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'