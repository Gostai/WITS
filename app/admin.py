from django.contrib import admin
from .models import Opinion
from .models import WitsUser

# Register your models here.

admin.site.register(WitsUser)
admin.site.register(Opinion)
