# Generated by Django 2.1.7 on 2019-04-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyLearn', '0005_auto_20190405_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcourses',
            name='SubjectID',
            field=models.CharField(max_length=12),
        ),
    ]
