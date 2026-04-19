from django.db import models
from django.contrib.auth.models import User


GENRE_CHOICES = [
    ('fantasy', 'Fantasy'),
    ('sci_fi', 'Sci-Fi'),
    ('romance', 'Romance'),
    ('misteri', 'Misteri'),
    ('thriller', 'Thriller'),
    ('horror', 'Horror'),
    ('historical', 'Historical Fiction'),
    ('literary', 'Literary Fiction'),
    ('adventure', 'Adventure'),
    ('dystopia', 'Dystopia'),
    ('biography', 'Biografi'),
    ('other', 'Lainnya'),
]


class BookReview(models.Model):
    # Foreign Key ke User bawaan Django
    # Kalau user dihapus, semua review-nya ikut terhapus (CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name='Judul Novel')
    author = models.CharField(max_length=255, verbose_name='Penulis')
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default='other',
        verbose_name='Genre'
    )
    review = models.TextField(verbose_name='Review')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Urutkan dari yang terbaru
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.author}"
