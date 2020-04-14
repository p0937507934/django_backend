from django.db.models import TextField,Model

# Create your models here.
class Device(Model):
    address=TextField(max_length=100)
    serial=TextField(max_length=100)