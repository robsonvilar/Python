from django import forms

class TecladoTelefoneForm(forms.Form):
    numero_telefone = forms.CharField(max_length=15, widget=forms.TextInput())
