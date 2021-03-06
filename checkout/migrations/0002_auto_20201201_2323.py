# Generated by Django 3.1.2 on 2020-12-01 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_class', '0009_workoutclass_sku'),
        ('products', '0003_product_model_id'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='workout_class',
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.CreateModel(
            name='OrderLineClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessions', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineclasses', to='checkout.order')),
                ('workout_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_class.workoutclass')),
            ],
        ),
    ]
