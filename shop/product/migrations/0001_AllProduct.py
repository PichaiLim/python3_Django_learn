# Generated by Django 3.1.7 on 2021-03-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_pricet', models.CharField(max_length=100)),
                ('product_detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
