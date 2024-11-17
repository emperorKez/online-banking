from fileinput import FileInput
from django import forms
from django.forms import ClearableFileInput, ImageField, FileField, DateInput
from django.core.files.uploadedfile import SimpleUploadedFile

from account.models import KYC

class DateInput(DateInput): 
    input_type = 'date'
    
class KYCForm(forms.ModelForm):
    image = ImageField(widget=forms.FileInput)
    identity_image = ImageField(widget=forms.FileInput)
    signature = ImageField(widget=forms.FileInput, required=True, error_messages={'blank': 'upload you signature', 'required': 'REQUIRED'})
    
    class Meta:
        model = KYC
        fields = ['firstname', 'lastname', 'gender', 'dob', 'marital_status', 'image', 'identity_image', 'identity_type','signature','country','city','street', 'state','mobile_phone']
        widgets = {
            'firstname': forms.TextInput(
                attrs={
                    'placeholder':'First Name',
                    'class':'',
                    'id':''
                }
            ),
            "lastname": forms.TextInput(attrs={ "placeholder":"Last Name"}),
            "mobile_phone": forms.TextInput(
                attrs={
                    "placeholder":"Mobile Phone",
                    "class":"",
                    "id":""
                }
            ),
            "mobile_phone": forms.TextInput(attrs={ "placeholder":"Mobile Phone"}),
            "street": forms.TextInput(attrs={ "placeholder":"Street"}),
            "city": forms.TextInput(attrs={ "placeholder":"City"}),
            "state": forms.TextInput(attrs={ "placeholder":"State"}),
            "dob": DateInput,
        }