# Generated by Django 2.2.7 on 2019-11-30 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20191129_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='piupiuwervicry_django\\media\\images\\defaultpic.png', upload_to='piupiuwervicry_django\\media\\images'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField()),
                ('joinedday', models.DateTimeField()),
                ('livingplace', models.CharField(max_length=50)),
                ('image', models.ImageField(default='piupiuwervicry_django\\media\\images\\defaultpic.png', upload_to='piupiuwervicry_django\\media\\images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
