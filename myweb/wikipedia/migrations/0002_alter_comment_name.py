# Generated by Django 4.1.2 on 2023-02-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(editable=False, max_length=15),
        ),
    ]
