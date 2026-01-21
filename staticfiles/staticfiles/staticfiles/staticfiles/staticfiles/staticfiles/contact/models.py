from django.db import models
# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15, default='N/A')
    message = models.TextField()
    submit = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.fullname
