# Generated by Django 2.1.2 on 2018-10-24 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('date_rls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinephilia',
            name='movies',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='date_rls.Movie'),
        ),
    ]
