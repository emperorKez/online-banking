from uuid import uuid4
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save

from userauth.models import User

ACCOUNT_STATUS = (('active', 'active'), ('inactive', 'inactive'))

MARITAL_STATUS = (('single', 'single'), ('married', 'married'), ('other', 'other'))

GENDER = (('male', 'male'), ('female', 'female'), ('other', 'other'))

NATIONALITY = (
    ('NG', 'Nigeria'),
    ('GH', 'Ghana'),  
    ('US', 'United States of America')
)

IDENTITY_TYPE =(
    ('national_id', 'National ID Card'),
    ('drivers_licence', 'Drivers Licence'),
    ('international_passport', 'International Passport')
)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(length=10, max_length=10, alphabet='1234567890')
    account_id = ShortUUIDField(length=10, max_length=13, prefix='kez', alphabet='1234567890')
    pin_number = ShortUUIDField(length=7, max_length=10, alphabet='1234567890')
    ref_code = ShortUUIDField(length=12, max_length=12, alphabet='abcdefg1234567890')
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default='inactive')
    date_created = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='recommended_by')
    
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return f"{self.user}"
    
class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    identity_image = models.ImageField(upload_to='kyc', default='default.jpg')
    gender = models.CharField(max_length=15, choices=GENDER)
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS)
    dob = models.DateField(auto_now_add=False)
    identity_type = models.CharField(max_length=100, choices=IDENTITY_TYPE)
    signature = models.ImageField(upload_to='kyc', blank=True)
    
    # contact detail
    country = models.CharField(max_length=100, choices=NATIONALITY)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    mobile_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user}"
        


        
    
    def create_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)
            
    def save_account(sender, instance, **kwargs):
        instance.account.save()
        
    post_save.connect(create_account, sender=User)
    post_save.connect(save_account, sender=User)
    