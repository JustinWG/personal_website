# Generated by Django 3.1.2 on 2020-11-02 14:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_journeystep_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeystep',
            name='title',
            field=tinymce.models.HTMLField(blank=True, max_length=50),
        ),
    ]
