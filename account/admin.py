from django.contrib import admin
from django import forms
from .models import *


class ProducerAdminForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'

    password = forms.CharField(widget=forms.PasswordInput)


class LimitsAdmin(admin.ModelAdmin):
    form = ProducerAdminForm


admin.site.register(Administrator, LimitsAdmin)
admin.site.register(StoreOwner, LimitsAdmin)
admin.site.register(StoreManager, LimitsAdmin)
admin.site.register(Producer, LimitsAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(Product)
