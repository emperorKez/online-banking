# Generated by Django 4.2.3 on 2023-07-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_kyc_country_alter_kyc_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='gender',
            field=models.CharField(choices=[(None, ''), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='', max_length=15),
        ),
    ]