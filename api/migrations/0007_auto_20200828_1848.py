# Generated by Django 2.2.8 on 2020-08-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200828_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_record',
            name='interest_rate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]