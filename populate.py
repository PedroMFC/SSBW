# populate.py
from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField, FileField
from datetime import datetime

connect('senderos', host='mongo')

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField, FileField
from datetime import datetime
from django import forms
from django.core.validators import RegexValidator, FileExtensionValidator

connect('senderos', host='mongo')

class Comentarios(EmbeddedDocument):
	contenido = StringField(required=True)
	autor     = StringField(max_length=120, required=True)
	fecha     = DateTimeField(default=datetime.now())

class Fotos(EmbeddedDocument):
	pie   = StringField(required=False, max_length=120)
	file  = StringField(required=False)

	def __str__(self):
		return self.pie

class Excursión(Document):
	nombre      = StringField(max_length=120, required=True)
	descripción = StringField(required=True)
	likes       = IntField(default=0)
	visitas     = IntField(default=0)
	tags        = ListField(StringField(max_length=20))
	duración    = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentarios))
	fotos       = ListField(EmbeddedDocumentField(Fotos))

	@property
	def foto(self):
		if len(self.fotos) > 0:
			return self.fotos[0].file
		else:
			return ''

	def __str__(self):
		return self.nombre

class ExcursiónForm(forms.Form):
	nombre      = forms.CharField(max_length=120)
	descripción = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40})),
	validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")]
	foto        = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
	pie 		= forms.CharField(max_length=80, required=False)

comentarios = [
	Comentarios(
        contenido = 'Primer comentario',
		autor = 'Yo'
	),
	Comentarios(
		contenido = 'Otro comentario',
		autor = 'Pepito'
    )
]

fotos = [
	Fotos(
		pie = 'Foto 1',
		file = 'imgs/senderos/sendero1.jpg'
	),
	Fotos(
		pie = 'Foto 2',
		file = 'imgs/senderos/sendero2.jpg'
	)
]

excursión = Excursión(nombre="Ruta en Granada", descripción="Bonita ruta por Granada", likes=1, 
                      tags=['fácil'], comentarios=comentarios, fotos = fotos)
excursión.save() # Para escribir en la BD

for excursión in Excursión.objects.all():
	print(excursión.nombre)
