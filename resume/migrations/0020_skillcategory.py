# Generated by Django 3.1.2 on 2020-12-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_auto_20201106_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
