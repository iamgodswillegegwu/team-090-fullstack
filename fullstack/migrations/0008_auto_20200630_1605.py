# Generated by Django 3.0.6 on 2020-06-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0007_auto_20200630_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='picture',
            field=models.FileField(upload_to='images/'),
        ),
    ]
