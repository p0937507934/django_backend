from django.db.models import CharField, Model, IntegerField, FloatField,TextField,ImageField
from django_mysql.models import ListCharField, JSONField
# Create your models here.

class Data(Model):
    Wavelength = JSONField()
    Intensity = JSONField()
    Reflectance = JSONField()
    Absorbance = JSONField()
    Config_id = IntegerField()
    user_id=IntegerField()
    device_id=IntegerField()
    img_path=ImageField(upload_to='pic/%Y%m%D')