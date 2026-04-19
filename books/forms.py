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
                'maxlength': 500,  # Batasi input di browser
            }),
        }

    def clean_review(self):
        """Validasi di server: review tidak boleh lebih dari 500 karakter."""
        review = self.cleaned_data.get('review', '')
        if len(review) > 500:
            raise forms.ValidationError('Review maksimal 500 karakter.')
        return review