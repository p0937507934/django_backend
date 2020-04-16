from django.db.models import CharField, Model, IntegerField, FloatField,TextField,ImageField
from django_mysql.models import ListCharField, JSONField

# Create your models here.

class Config(Model):
    scan_type = IntegerField()
    start_wave = IntegerField()
    end_wave = IntegerField()
    wave_width = FloatField()
    num_repeat = IntegerField()
    exposure_time = FloatField()
    num_point = IntegerField()
