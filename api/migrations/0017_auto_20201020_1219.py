# Generated by Django 3.1.2 on 2020-10-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20201020_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=80, null=True, verbose_name='书名'),
        ),
    ]
