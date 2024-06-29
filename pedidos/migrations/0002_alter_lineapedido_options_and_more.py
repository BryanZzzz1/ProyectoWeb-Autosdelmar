# Generated by Django 4.1.2 on 2024-06-28 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineapedido',
            options={'ordering': ['id'], 'verbose_name': 'linea de pedido', 'verbose_name_plural': 'lineas de pedido'},
        ),
        migrations.AlterField(
            model_name='lineapedido',
            name='pedido_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineas_pedido', to='pedidos.pedido'),
        ),
        migrations.AlterModelTable(
            name='lineapedido',
            table='lineas_pedidos',
        ),
    ]
