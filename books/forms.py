from django import forms
from .models import BookReview


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        # Field yang muncul di form (user tidak perlu diisi manual)
        fields = ['title', 'author', 'genre', 'review']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: The Name of the Wind',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Patrick Rothfuss',
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select',
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Ceritakan pendapatmu tentang novel ini...',
            }),
        }
