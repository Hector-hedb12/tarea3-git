# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('is_up_me', '0001_initial')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(verbose_name='fecha consultada'),
            name = 'consulta_date',
            model_name = 'historial',
        ),
    ]
