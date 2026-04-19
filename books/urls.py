from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Books
    path('', views.dashboard, name='dashboard'),
    path('tambah/', views.add_book, name='add_book'),
    path('buku/<int:pk>/', views.book_detail, name='book_detail'),
    path('buku/<int:pk>/hapus/', views.delete_book, name='delete_book'),
]
