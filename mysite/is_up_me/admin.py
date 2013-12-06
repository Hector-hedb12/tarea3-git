from django.contrib import admin
from is_up_me.models import Historial

class HistorialAdmin(admin.ModelAdmin):
    list_display = ('url_text', 'consulta_date', 'fue_consultada_recientemente')
    list_filter = ['consulta_date']
    search_fields = ['url_text']
  

admin.site.register(Historial, HistorialAdmin)