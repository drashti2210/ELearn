# Generated by Django 2.1.7 on 2019-04-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyLearn', '0007_reviewcourses_studentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcourses',
            name='Sname',
            field=models.CharField(default='', max_length=12),
        ),
    ]
