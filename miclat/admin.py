from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import MiclatData, MiclatLog

# Register your models here.
@admin.register(MiclatData)
class MiclatDataImportExport(ImportExportModelAdmin):
    fields = [
        'code',
        'nin',
        'sexe',
        'acteN',
        'annee',
        'nom_a',
        'nom_f',
        'd_nais',
        'h_nais',
        'pren_a',
        'pren_f',
        'presume',
        'codecomm',
        'nom_mere',
        'lieu_nais',
        'pren_mere',
        'decesMentions',
        'divorceMentions',
        'mariageMentions',
        'data',
        'active',
       
    ]

    list_display = [
        'code',
        'nin',
        'nom_f',
        'pren_f',
        'presume',
        'created_at',
        'update_in',
        'active',
        
       
    ]

    search_fields = ['active']
    list_filter = ['active']


@admin.register(MiclatLog)
class MiclatLogImportExport(ImportExportModelAdmin):
    fields = [
        'nin',
        'status',
        'response_code',
        'message',
        'response_data',
        'active',
       
    ]

    list_display = [
        'code',
        'nin',
        'status',
        'response_code',
        'created_at',
        'update_in',
        'active',
        
       
    ]

    search_fields = ['active']
    list_filter = ['active']