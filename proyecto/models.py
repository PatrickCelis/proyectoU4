from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    foto = ImageField(upload_to='proyecto/images/')
    title = CharField(max_length=50)
    descripcion = CharField(max_length=500)
    tags = CharField(max_length=20)
    github = URLField(blank=True)
    class Meta:
        db_table: "proyecto_project"

