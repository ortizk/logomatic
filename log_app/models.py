from django.db import models

class User(models.Models):
        name = models.CharField(max_length = 100)
        email = models.EmailField()
        system_type = models.Charfield(max_length = 100)
        cart_numbers = models.Charfield(max_length = 20)