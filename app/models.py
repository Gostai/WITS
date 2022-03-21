from django.db import models
from .utilities import get_timestamp_path
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification

# Create your models here.

user_registrated = Signal(providing_args=['instance'])

def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])
    
user_registrated.connect(user_registrated_dispatcher)

class WitsUser(AbstractUser):
    is_activated = models.BooleanField(default = False, db_index=True)
    send_messages = models.BooleanField(default=False)
    
    class Meta(AbstractUser.Meta):
        pass


class Opinion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True, default='')
    #coords = models.JSONField(blank=True)
    caption = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to=get_timestamp_path, blank=True)
    owner = models.ForeignKey('WitsUser', related_name='opinions', on_delete=models.CASCADE)
    SNOW_LEVEL_CHOICES = (
        ('L','LOW'),
        ('M','MEDIUM'),
        ('H','HIGH'),
        )
    level = models.CharField(max_length=1, choices=SNOW_LEVEL_CHOICES, default='L')
    
    class Meta:
        ordering = ['created']
        
