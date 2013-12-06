# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('url_text', models.CharField(max_length=400),), ('consulta_date', models.DateTimeField(verbose_name='fecha de consulta'),)],
            bases = (models.Model,),
            options = {},
            name = 'Historial',
        ),
    ]
