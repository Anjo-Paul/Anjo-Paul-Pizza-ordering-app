

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('size', models.CharField(blank=True, max_length=5)),
                ('toppings', models.CharField(blank=True, max_length=100)),
                ('num_toppings', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='orders', to='orders.Item'),
        ),
    ]
