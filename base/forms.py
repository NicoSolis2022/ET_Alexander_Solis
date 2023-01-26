from django import forms
from django.forms import ModelForm 
from django.forms import widgets 
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from .models import cliente

class clienteform(forms.ModelForm):

    class meta: 
        model = cliente
        fields = ['rut', 'nombre', 'email', 'clave']
        labels = {
            'rut': 'rut',
            'nombre': 'nombre',
            'email': 'email',
            'clave': 'clave',
        
        }
        widgets={
            'rut': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'digite su rut',
                    'id' : 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'digite su nombre',
                    'id' : 'nombre'
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'digite su email',
                    'id' : 'email'
                }
            ),
            'clave': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'digite su clave',
                    'id' : 'clave'
                }
            )
        }