# Generated by Django 3.2.7 on 2022-01-18 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='currency.source'),
        ),
    ]
