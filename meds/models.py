from django.db import models

class medicine(models.Model):
    name = models.CharField(max_length=100)
    side_effects = models.TextField()

    def __str__(self):
        return self.name

class uses(models.Model):
    name = models.CharField(max_length=50)
    descritpiton = models.TextField()
    medicines = models.ManyToManyField(medicine, related_name="uses")

    def __str__(self):
        return self.name
    

