from django.contrib import admin

from .models import *

admin.site.register(StoreOwner)
admin.site.register(StoreManager)
admin.site.register(Producer)
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(Product)
