"""
permite que una clase se extienda con nuevas características para que luego se vuelva un formulario de html
crear_tarea_col_titulo: no es para la base de datos, es para enviarselo al html y lo transforma en un input de tipo texto
forms da una propiedad para heredar su clase llamada Form
widget=forms.Textarea: si queremos que sea text area, heredado desde forms.textarea
widget=forms.TextInput(attrs={class:''}): para agregar estilos a formulario"""

from django import forms

class tf_cuerpo (forms.Form):

    cuerpo = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: PARTE DEL CUERPO'
    }))


class tf_ejercicio (forms.Form):

    cuerpo = forms.IntegerField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: # PARTE DE CUERPO'
    }))

    ejercicio = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: EJERCICIO'
    }))

    posicion = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: POSICIÓN'
    }))

    tipo = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: TIPO'
    }))

    repeticiones = forms.IntegerField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: # REPETICIONES'
    }))