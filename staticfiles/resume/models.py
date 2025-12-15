from django.db import models


# Create your models here.


class Experience(models.Model):
    # experience list
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    experience_description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.office_name}({self.from_date} to {self.to_date})"
    # education


class Education(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    institution_name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name} ({self.from_date} to {self.to_date or 'Present'})"


class Professionalskill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
