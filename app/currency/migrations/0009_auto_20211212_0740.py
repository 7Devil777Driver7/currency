# Generated by Django 3.2.7 on 2021-12-12 07:40
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_rate_cur_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='User', max_length=255),
        ),
        migrations.AddField(
            model_name='contactus',
            name='raw_content',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=1024),
        ),
    ]
