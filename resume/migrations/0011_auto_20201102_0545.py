# Generated by Django 3.1.2 on 2020-11-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20201102_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='detailed_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lessons_learned',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_used',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='to_do',
            field=models.TextField(blank=True),
        ),
    ]
