# Generated by Django 2.2.7 on 2019-11-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='handle',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
