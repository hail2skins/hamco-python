# Generated by Django 5.0.4 on 2024-04-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='street_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='zip_code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
