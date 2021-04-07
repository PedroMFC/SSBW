#from django.db import models

# Create your models here.

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField, FileField
from datetime import datetime

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