from django.db import models

# Create your models here.

class Blogs(models.Model):

    title = models.CharField(max_length=40)
    explanation = models.TextField(max_length=500)
    source = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    cratedat= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title    


