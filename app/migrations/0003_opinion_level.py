# Generated by Django 3.1.5 on 2021-01-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210125_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='level',
            field=models.CharField(choices=[('L', 'LOW'), ('M', 'MEDIUM'), ('H', 'HIGH')], default='L', max_length=1),
            preserve_default=False,
        ),
    ]
