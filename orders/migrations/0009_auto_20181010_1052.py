

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20181010_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(blank=True, max_length=5)),
                ('extra', models.ManyToManyField(blank=True, related_name='item', to='orders.SubExtra')),
                ('toppings', models.ManyToManyField(blank=True, related_name='item', to='orders.PizzaTopping')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='item',
            name='toppings',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='orders', to='orders.OrderItem'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
