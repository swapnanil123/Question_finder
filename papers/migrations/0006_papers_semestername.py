# Generated by Django 3.1.3 on 2021-02-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20210206_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='semesterName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
