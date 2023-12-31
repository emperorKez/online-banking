# Generated by Django 4.2.3 on 2023-07-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_kyc_city_alter_kyc_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='country',
            field=models.CharField(choices=[('NG', 'Nigeria'), ('GH', 'Ghana'), ('US', 'United States of America')], default='ng', max_length=100),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=15),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='identity_type',
            field=models.CharField(choices=[('national_id', 'National ID Card'), ('drivers_licence', 'Drivers Licence'), ('international_passport', 'International Passport')], default='drivers_licence', max_length=100),
        ),
    ]
