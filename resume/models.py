from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.utils.dates import MONTHS
from tinymce import models as tinymce_models


class JourneyStep(models.Model):
    day_choices = [(x, x) for x in range(1, 31)]
    month_choices = (list(MONTHS.items()))
    year_choices = [(x, x) for x in range(1900, datetime.now().year+1)]
    employer = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    start_day = models.IntegerField(choices=day_choices, blank=True, null=True)
    start_month = models.IntegerField(choices=month_choices, blank=True, null=True)
    start_year = models.IntegerField(choices=year_choices, blank=True, null=True)
    end_day = models.IntegerField(choices=day_choices, blank=True, null=True)
    end_month = models.IntegerField(choices=month_choices, blank=True, null=True)
    end_year = models.IntegerField(choices=year_choices, blank=True, null=True)
    cover_image = models.ImageField(upload_to='journeys/', null=True)
    description = models.TextField(null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.employer


class Project(models.Model):
    title = models.CharField(max_length=50)
    accomplished = tinymce_models.HTMLField(blank=True)
    tech_used = tinymce_models.HTMLField(blank=True)
    lessons_learned = tinymce_models.HTMLField(blank=True)
    to_do = tinymce_models.HTMLField(blank=True)
    detailed_description = tinymce_models.HTMLField(blank=True)
    link = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(default=None, null=True, blank=True,
                                validators=[MaxValueValidator(5), MinValueValidator(1)])
    category = models.ForeignKey('SkillCategory', on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"{self.name} {self.stars} stars"


class Connect(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='connect/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name
