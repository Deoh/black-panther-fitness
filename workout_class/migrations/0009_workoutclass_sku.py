# Generated by Django 3.1.2 on 2020-11-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_class', '0008_auto_20201129_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutclass',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
