# Generated by Django 2.0.6 on 2018-06-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
