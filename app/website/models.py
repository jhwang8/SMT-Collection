from django.db import models

# Create your models here.
class Demon(models.Model):
    name = models.TextField()
    race = models.TextField()
    physical = models.TextField()
    fire = models.TextField()
    ice = models.TextField()
    electricity = models.TextField()
    force = models.TextField()
    mystic = models.TextField()

    class Meta:
        db_table = 'demons'