from django.db import models

class Property(models.Model):
  rental_income = models.FloatField(default=0)
  laundry_income = models.FloatField(default=0)
  storage_income = models.FloatField(default=0)
  misc_income = models.FloatField(default=0)
  
