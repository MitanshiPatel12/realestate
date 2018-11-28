from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PermissionType,SysFeatureRole,RoleCode,SysFeature,UserRole,Property, PropertyCategory,PropertySector,PropertyFacing, PropertyImages,Country,City,Province

admin.site.register(Property)
admin.site.register(PropertyCategory)
admin.site.register(PropertySector)
admin.site.register(PropertyFacing)
admin.site.register(PropertyImages)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(UserRole)
admin.site.register(SysFeature)
admin.site.register(RoleCode)
admin.site.register(SysFeatureRole)
admin.site.register(PermissionType)

