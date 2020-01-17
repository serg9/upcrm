# Generated by Django 3.0.2 on 2020-01-15 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dict', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
