from uuid import uuid4
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save

from userauth.models import User

ACCOUNT_STATUS = (('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending'))

MARITAL_STATUS = ((None, ''),('single', 'Single'), ('married', 'Married'), ('other', 'Other'))

GENDER = ((None, ''),('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

NATIONALITY = ((None, ''),
    ('NG', 'Nigeria'),
    ('GH', 'Ghana'),  
    ('US', 'United States of America')
)

IDENTITY_TYPE =((None, ''),
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
    account = models.OneToOneField(Account, on_delete=models.CASCADE, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=False, null=False,)
    lastname = models.CharField(max_length=100, blank=False, null=False,)
    image = models.ImageField(upload_to='kyc', default='default.jpg', editable=True, error_messages={'required': 'Required'})
    identity_image = models.ImageField(upload_to='kyc', default='default.jpg')
    gender = models.CharField(max_length=15, choices=GENDER, blank=False, null=False, default='', error_messages={'required': 'Required'})
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS, default='', error_messages={'required': 'Required'})
    dob = models.DateField(auto_now_add=False, blank=False, null=False)
    identity_type = models.CharField(max_length=100, choices=IDENTITY_TYPE, default='')
    signature = models.ImageField(upload_to='kyc', blank=True)
    
    # contact detail
    country = models.CharField(max_length=100, choices=NATIONALITY, default='ng')
    city = models.CharField(max_length=100, blank=False, null=False,)
    street = models.CharField(max_length=150, blank=False, null=False,)
    state = models.CharField(max_length=150, blank=False, null=False,)
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
    