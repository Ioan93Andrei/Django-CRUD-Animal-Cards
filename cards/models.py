from django.db import models

# Create your models here.
class Card(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name