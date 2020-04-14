from django.db.models import CharField, Model, IntegerField, FloatField,TextField,ImageField
from django_mysql.models import ListCharField, JSONField

# Create your models here.

class Config(Model):
    Scantype = IntegerField()
    Start_wave = IntegerField()
    End_wave = IntegerField()
    Wave_width = FloatField()
    Num_repeat = IntegerField()
    Exposure_time = FloatField()
    Num_point = IntegerField()
