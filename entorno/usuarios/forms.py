from django import forms
from .models import *
#from django.forms import ModelForm
#from .models import tabla_prueba, driver, client, producer
#from django.db import models
#from django.forms import ModelForm

class form_soporte(forms.ModelForm):
    class Meta:
        model = soporte
        fields = '__all__'

class registro_usuario(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class registro_profesional(forms.ModelForm):
    class Meta:
        model = profesional
        fields = '__all__'
