# Generated by Django 4.2.3 on 2023-07-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_kyc_country_alter_kyc_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=15),
        ),
    ]