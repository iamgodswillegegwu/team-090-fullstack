# Generated by Django 3.0.6 on 2020-05-23 19:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0009_add_subregion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('picture', models.ImageField(upload_to='uploads/')),
                ('description', models.TextField(max_length=200)),
                ('years_of_experience', models.IntegerField()),
                ('year_of_establishement', models.DateField(default=django.utils.timezone.now)),
                ('supporting_document', models.FileField(null=True, upload_to='uploads/')),
                ('rating', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack.Category')),
                ('service_rendered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack.Service')),
            ],
        ),
    ]