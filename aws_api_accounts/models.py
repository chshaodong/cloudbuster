from django.db import models
from cloudbuster.encryption import EncryptedCharField

class AWSAPIAccount(models.Model):
    name = models.CharField(max_length=255)
    access_id = models.CharField(max_length=255)
    secret_key = EncryptedCharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
