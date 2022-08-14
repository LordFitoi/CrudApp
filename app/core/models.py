import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True
    

class Entity(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'Active'
        INACTIVE = 'Inactive'

    class Role(models.TextChoices):
        ADMIN = 'Admin'
        MODERATOR = 'Moderator'
        USER = 'User'
    
    class DocumentTypes(models.TextChoices):
        RNC = "RNC"
        IDCard = "ID Card"
        Passport = "Passport"
    
    class EntityTypes(models.TextChoices):
        Physical = "Physical"
        Juridical = "Juridical"

    description = models.CharField(max_length=120)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    state = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    phone_number = models.CharField(max_length=60)
    is_deletable = models.BooleanField(default=False)

    # Location Data:
    address = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Document Data:
    document_type = models.CharField(max_length=9, choices=DocumentTypes.choices, default=DocumentTypes.RNC)
    entity_type = models.CharField(max_length=9, choices=EntityTypes.choices,
        default=EntityTypes.Juridical)
    number = models.CharField(max_length=15)

    # Social Media Data:
    website_url = models.URLField(max_length=120, blank=True, null=True)
    facebook_url = models.URLField(max_length=120, blank=True, null=True)
    instagram_url = models.URLField(max_length=120, blank=True, null=True)
    twitter_url = models.URLField(max_length=120, blank=True, null=True)
    tiktok_url = models.URLField(max_length=120, blank=True, null=True)