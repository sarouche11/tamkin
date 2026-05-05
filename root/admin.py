from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.

@admin.register(Wilaya)
class WilayaImportExport(ImportExportModelAdmin):
    fields = [
        'code',
        'name_fr',
        'name_ar',
        'active',
    ]
    list_display = [
        'code',
        'name_fr',
        'name_ar',
        'active',
        'insert_in',
        'updated_in'
    ]
    search_fields = ['code', 'name_fr', 'name_ar']  # Allows search by these fields
    list_filter = ['active']  # Allows filtering by active status
    ordering = ['code'] 

@admin.register(Commune)
class CommuneImportExport(ImportExportModelAdmin):
    fields = [
        'code',
        'name_fr',
        'name_ar',
        'wilaya',
        'active',
    ]
    list_display = [
        'code',
        'name_fr',
        'name_ar',
        'wilaya',
        'active',
        'insert_in',
        'updated_in'
    ]
    search_fields = ['code', 'name_fr', 'name_ar']  # Allows search by these fields
    list_filter = ['active']  # Allows filtering by active status
    ordering = ['code'] 

@admin.register(Registered)
class RegisteredImportExport(ImportExportModelAdmin):
    fields = [
        'nin',
        'first_name',
        'last_name',
        'genre',
        'birthday',
        'phone',
        'wilaya',
        'status',
        'miclat',
        'active',
    ]
    list_display = [
        'code',
        'compagnion',
        'nin',
        'first_name',
        'last_name',
        'genre',
        'birthday',
        'phone',
        'wilaya',
        'status',
        'miclat',
        'active',
        'insert_in',
        'updated_in'
    ]
    search_fields = ['code', 'nin', 'first_name','last_name']  # Allows search by these fields
    list_filter = ['active']  # Allows filtering by active status
    ordering = ['code'] 

@admin.register(Compagnion)
class CompagnionImportExport(ImportExportModelAdmin):
    fields = [
        'code',
        'nin',
        'user',
        'genre',
        'birthday',
        'phone',
       
        'active',
    ]
    list_display = [
        'code',
        'nin',
        'user',
        'genre',
        'birthday',
        'phone',
       
        'active',
        'insert_in',
        'updated_in'
    ]
    search_fields = ['code', 'nin', 'first_name','last_name']  # Allows search by these fields
    list_filter = ['active']  # Allows filtering by active status
    ordering = ['code'] 