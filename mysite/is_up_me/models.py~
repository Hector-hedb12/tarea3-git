from django.db import models
import datetime
from django.utils import timezone

class Historial(models.Model):
    url_text = models.CharField(max_length=400)
    consulta_date = models.DateTimeField('fecha consultada')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.url_text
      
    def fue_consultada_recientemente(self):
        return self.consulta_date >= timezone.now() - datetime.timedelta(days=1)
    fue_consultada_recientemente.admin_order_field = 'consulta_date'
    fue_consultada_recientemente.boolean = True
    fue_consultada_recientemente.short_description = 'Consultada recientemente?'

