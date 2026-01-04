from django.core.exceptions import ValidationError
from django.db import models


class Homepage(models.Model):
    # banner section
    label = models.CharField(max_length=100)
    mini_title = models.CharField(max_length=100)
    max_title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    # about section
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and Homepage.objects.exists():
            raise ValidationError(
                message="Only one Homepage instance is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Homepage Content"
