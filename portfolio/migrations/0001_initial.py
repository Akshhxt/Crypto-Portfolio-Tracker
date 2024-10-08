# Generated by Django 5.1.1 on 2024-09-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
