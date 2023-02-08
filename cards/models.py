from django.db import models

# Create your models here.
class Card(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.name

class Blog(models.Model):
    text = models.TextField(max_length=750)
    pub_date = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.text