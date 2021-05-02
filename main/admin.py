from django.contrib import admin
from .models import Exhibit
# Register your models here.

class ExhibitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exhibit,ExhibitAdmin)