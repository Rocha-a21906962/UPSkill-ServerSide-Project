from django.db import models

# Create your models here.


class Actor(models.Model):

    name = models.CharField(max_length=200)
    # Date of birt...
    dob = models.DateField(default=None, blank=True, null=True)
    pic = models.ImageField(upload_to="actor/%Y/%m/%d/", blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        pass