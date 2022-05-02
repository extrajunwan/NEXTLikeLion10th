from django.db import models

# Create your models here.
class Major(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return f'[{self.pk}]{self.name}'

    


