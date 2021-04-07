from django import forms
from django.core.validators import RegexValidator, FileExtensionValidator

class ExcursiónForm(forms.Form):
	nombre      = forms.CharField(max_length=120)
	descripción = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}), validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")])
	foto        = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
	pie 		= forms.CharField(max_length=80, required=False)