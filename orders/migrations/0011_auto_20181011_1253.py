

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0010_auto_20181010_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='placed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
