# Generated by Django 3.1.3 on 2021-01-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='questionPaperURL',
            field=models.CharField(default='', max_length=550),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='questionPaperName',
            field=models.CharField(default='', max_length=350),
        ),
    ]
