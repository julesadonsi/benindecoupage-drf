# Generated by Django 5.0.1 on 2024-01-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_district_id_deighborhoods_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deighborhoods',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
