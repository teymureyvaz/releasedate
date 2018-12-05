# Generated by Django 2.1.2 on 2018-10-25 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('date_rls', '0005_auto_20181024_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermovie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='usermovie',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserMovie',
        ),
    ]
