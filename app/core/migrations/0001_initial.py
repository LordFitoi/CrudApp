# Generated by Django 4.0.3 on 2022-08-14 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=120)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Moderator', 'Moderator'), ('User', 'User')], default='User', max_length=10)),
                ('state', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('phone_number', models.CharField(max_length=60)),
                ('is_deletable', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=40)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('document_type', models.CharField(choices=[('RNC', 'Rnc'), ('ID Card', 'Idcard'), ('Passport', 'Passport')], default='RNC', max_length=9)),
                ('entity_type', models.CharField(choices=[('Physical', 'Physical'), ('Juridical', 'Juridical')], default='Juridical', max_length=9)),
                ('number', models.CharField(max_length=15)),
                ('website_url', models.URLField(blank=True, max_length=120, null=True)),
                ('facebook_url', models.URLField(blank=True, max_length=120, null=True)),
                ('instagram_url', models.URLField(blank=True, max_length=120, null=True)),
                ('twitter_url', models.URLField(blank=True, max_length=120, null=True)),
                ('tiktok_url', models.URLField(blank=True, max_length=120, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
