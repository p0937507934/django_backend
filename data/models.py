from django.db.models import CharField, Model, IntegerField, FloatField, TextField, ImageField, FileField,DateTimeField
from django_mysql.models import ListCharField, JSONField
from django.utils.timezone import now
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
    level=IntegerField()
    confidence=FloatField()
    Measurement_Date=DateTimeField(default=now)

    def __str__(self):
        return str(self.Measurement_Date.strftime('%Y/%m/%d %I:%M %p'))+'---'+str(self.product_serial)

class DataCheck(Model):
    wavelength = JSONField(default=list)
    intensity = JSONField(default=list)
    reflectance = JSONField(default=list)
    absorbance = JSONField(default=list)
    config_id = IntegerField()
    device_serial = TextField()
    product_serial=TextField()
    img = FileField()
