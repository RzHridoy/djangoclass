from django.contrib import admin
from classView import models

# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'amount', 'status']


admin.site.register(models.Data)
admin.site.register(models.Payment, PaymentAdmin)