

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_orderitem_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
