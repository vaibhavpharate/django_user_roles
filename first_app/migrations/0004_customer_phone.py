# Generated by Django 3.2.3 on 2021-05-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=5898745865, max_length=13),
            preserve_default=False,
        ),
    ]