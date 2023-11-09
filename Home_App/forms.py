from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

    def clean(self):
        cleaned_data = super().clean()
        images_count = Image.objects.count()
        if images_count >= 12:
            raise forms.ValidationError("You've reached the maximum limit of 12 images.")
