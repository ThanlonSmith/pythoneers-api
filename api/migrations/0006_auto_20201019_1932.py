# Generated by Django 3.1.2 on 2020-10-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_banner_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': 'Banner'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banner/', verbose_name='Banner链接'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Banner标题'),
        ),
    ]
