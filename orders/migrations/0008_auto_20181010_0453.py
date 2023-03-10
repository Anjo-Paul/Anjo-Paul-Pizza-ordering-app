

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('orders', '0007_auto_20181010_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Topping',
            new_name='PizzaTopping',
        ),
        migrations.AddField(
            model_name='item',
            name='extra',
            field=models.ManyToManyField(blank=True, related_name='item', to='orders.SubExtra'),
        ),
    ]
