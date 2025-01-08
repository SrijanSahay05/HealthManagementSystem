from django.db import models


class uses(models.Model):
    name = models.CharField(max_length=50)
    descripiton = models.TextField()
        

    def __str__(self):
        return self.name
    
class medicine(models.Model):
    name = models.CharField(max_length=100)
    side_effects = models.TextField()
    uses = models.ManyToManyField(uses, related_name="medicine")


    def __str__(self):
        return self.name
    

