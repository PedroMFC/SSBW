#from django.db import models

# Create your models here.

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField, FileField
from datetime import datetime
from django.core.validators import RegexValidator, FileExtensionValidator
#from rest_framework_mongoengine import serializers
from rest_framework import serializers

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

# SERIALIZERS
class ExcursiónSerializer(serializers.Serializer):
	nombre = serializers.CharField(max_length = 20)
	descripción = serializers.CharField(validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")])
	foto = serializers.FileField(required=False, allow_null='true', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
	pie = serializers.CharField(max_length=80, required=False)

	def create(self, validated_data):
		return Excursión.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.nombre = validated_data.get('nombre', instance.nombre)
		instance.descripción = validated_data.get('descripción', instance.descripción)
		instance.foto = validated_data.get('foto', instance.foto)
		instance.pie = validated_data.get('pie', instance.pie)
		
		instance.save()
		return instance

'''
class ExcursiónSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Excursión
		fields = ['nombre', 'descripción']
'''
