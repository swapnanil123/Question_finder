# Generated by Django 3.1.3 on 2021-02-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20210126_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpaper',
            name='questionPaperName',
        ),
        migrations.RemoveField(
            model_name='questionpaper',
            name='questionPaperURL',
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='qtnFile',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
