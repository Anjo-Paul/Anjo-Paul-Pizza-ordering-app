

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20181010_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='extra',
            field=models.ManyToManyField(blank=True, related_name='sub', to='orders.SubExtra'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizza', to='orders.PizzaTopping'),
        ),
    ]
