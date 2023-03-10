

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_orderitem_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.OrderItem'),
        ),
    ]
