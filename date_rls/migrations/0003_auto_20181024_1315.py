# Generated by Django 2.1.2 on 2018-10-24 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('date_rls', '0002_auto_20181024_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinephilia',
            name='movies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='date_rls.Movie'),
        ),
    ]
