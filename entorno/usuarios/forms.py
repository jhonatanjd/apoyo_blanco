from django import forms
from .models import *
#from django.forms import ModelForm
#from .models import tabla_prueba, driver, client, producer
#from django.db import model
#from django.forms import ModelForm




class form_soporte(forms.ModelForm):
    class Meta:
        model = soporte
        fields = '__all__'