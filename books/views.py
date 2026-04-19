from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import BookReview
from .forms import BookReviewForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    books = BookReview.objects.filter(user=request.user)
    return render(request, 'books/dashboard.html', {
        'books': books,
        'total': books.count(),
    })


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('dashboard')
    else:
        form = BookReviewForm()

    return render(request, 'books/add_book.html', {'form': form})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(BookReview, pk=pk, user=request.user)
    return render(request, 'books/detail.html', {'book': book})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(BookReview, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('dashboard')
    return redirect('book_detail', pk=pk)
