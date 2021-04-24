# Generated by Django 3.2 on 2021-04-23 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('price', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
