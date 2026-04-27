from django.contrib import admin
from .models import Abonne

class AbonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')

admin.site.register(Abonne, AbonneAdmin)
