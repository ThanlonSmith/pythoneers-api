# Generated by Django 3.1.2 on 2020-10-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201019_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='source',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='链接到的url'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banner/', verbose_name='图片链接'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='标题'),
        ),
    ]