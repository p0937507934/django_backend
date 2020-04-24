from django.db.models import CharField, Model, IntegerField, FloatField, TextField, ImageField, FileField
from django_mysql.models import ListCharField, JSONField
# Create your models here.


class Data(Model):
    wavelength = JSONField(default=list)
    intensity = JSONField(default=list)
    reflectance = JSONField(default=list)
    absorbance = JSONField(default=list)
    config_id = IntegerField()
    user_id = IntegerField()
    device_id = IntegerField()
    product_serial=TextField()
    img = ImageField(upload_to='pic/%Y/%m/%D')
    label=IntegerField()
    confidence=FloatField()


class DataCheck(Model):
    wavelength = JSONField(default=list)
    intensity = JSONField(default=list)
    reflectance = JSONField(default=list)
    absorbance = JSONField(default=list)
    config_id = IntegerField()
    device_serial = TextField()
    product_serial=TextField()
    img = FileField()
