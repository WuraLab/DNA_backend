# Generated by Django 3.0.8 on 2020-08-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200801_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_record',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]