import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='rate', to='currency.source'
                ),
        ),
    ]
