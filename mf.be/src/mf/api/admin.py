from django.contrib import admin
from .models import *



@admin.register(PartnerTask)
class PartnerTaskAdmin(admin.ModelAdmin):
    ...


# Register your models here.
