

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='num_toppings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
