
from django import forms
from .models import Status, Role, DocumentTypes, EntityTypes


class EntityForm(forms.Form):
    description = forms.CharField(max_length=120)
    role = forms.ChoiceField(choices=Role.choices)
    state = forms.ChoiceField(choices=Status.choices)
    credit_limit = forms.DecimalField(max_digits=15, decimal_places=2)
    phone_number = forms.CharField(max_length=60)
    is_deletable = forms.BooleanField()

    # Location Data:
    address = forms.CharField(max_length=40)
    postal_code = forms.CharField(max_length=10)
    latitude = forms.DecimalField(max_digits=9)
    longitude = forms.DecimalField()
    
    # Document Data:
    document_type = forms.ChoiceField(choices=DocumentTypes.choices)
    entity_type = forms.ChoiceField(choices=EntityTypes.choices)
    number = forms.CharField(max_length=15)

    # Social Media Data:
    website_url = forms.URLField(max_length=120)
    facebook_url = forms.URLField(max_length=120)
    instagram_url = forms.URLField(max_length=120)
    twitter_url = forms.URLField(max_length=120)
    tiktok_url = forms.URLField(max_length=120)
