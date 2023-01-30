from django.db import models

# Create your models here.
class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length = 32)
    description = models.TextField(null=True, blank=True)
    #participants = 
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.name)
