from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class CleinteAdm(admin.ModelAdmin):
    list_display = ['nome','endereco','idade']