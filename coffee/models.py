from django.contrib.auth import get_user_model
from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=64)
    maker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
