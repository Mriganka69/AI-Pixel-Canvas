from django import forms
from .models import ImageAsset  # Make sure you have the model

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageAsset
        fields = ['image']

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
