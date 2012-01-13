"Register the Asset model with the Admin application"
from django.contrib import admin
from models import Asset 

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_location', )
    pass

admin.site.register(Asset, AssetAdmin)
