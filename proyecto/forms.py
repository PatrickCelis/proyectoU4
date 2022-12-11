from django import forms
from proyecto.models import Project


class ProyectoForm(forms.ModelForm):
    foto = forms.ImageField()
    title = forms.CharField()
    descripcion = forms.CharField(label="Descripción",widget=forms.Textarea(attrs={"rows":3}))
    tags = forms.CharField()
    github = forms.URLField()

    class Meta:
        model = Project
        fields = ['foto','title','descripcion','tags','github']