# Generated by Django 4.2.3 on 2023-07-22 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_alter_account_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='kyc')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=15)),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('other', 'other')], max_length=15)),
                ('dob', models.DateTimeField()),
                ('identity_type', models.CharField(choices=[('national_id', 'National ID Card'), ('drivers_licence', 'Drivers Licence'), ('international_passport', 'International Passport')], max_length=100)),
                ('signature', models.ImageField(default='default.jpg', upload_to='kyc')),
                ('country', models.CharField(choices=[('NG', 'Nigeria'), ('GH', 'Ghana'), ('US', 'United States of America')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
