# Generated by Django 2.2.7 on 2019-11-30 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='piupiuwervicry_django\\django_treinamento\\piupiuwervicry_django\\media\\images\\defaultpic.png', upload_to='piupiuwervicry_django\\django_treinamento\\piupiuwervicry_django\\media\\images')),
                ('birthday', models.DateTimeField()),
                ('joinedday', models.DateTimeField()),
                ('livingplace', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
