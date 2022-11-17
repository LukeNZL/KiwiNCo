# Generated by Django 4.1.3 on 2022-11-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_carteditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(default=0, max_length=30)),
                ('itemSize', models.CharField(max_length=3)),
                ('buyerId', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='carteditem',
            name='itemName',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='ItemName',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
