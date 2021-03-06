from django import forms

class FormArticulo(forms.Form):

    titulo = forms.CharField(
        label="Titulo"
    )

    contenido = forms.CharField(
        label="Contenido",
        widget= forms.Textarea
    )

    opciones_publicado = [
        (1, 'SI'),
        (0, 'NO')
    ]

    publicado = forms.TypedChoiceField (
        label= "¿Publicado?",
        choices= opciones_publicado
    )