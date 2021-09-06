from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=128, blank=True)
    message = models.CharField(max_length=256, blank=True)

    def __str__(self,):
        return self.from_email

    def __str__(self):
        return self.subject

    def __str__(str):
        return self.message
