from django.db import models
from django.contrib.auth.models import User

class pdfQR(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=300)