from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import BookReview

def landing_page(request):
    return render(request, 'landing.html')

def home_page(request):
    book_reviews = BookReview.objects.all().order_by('-created_at')
    page_size=request.GET.get('page_size', 4)
    paginator = Paginator(book_reviews, page_size)

    page_num=request.GET.get('page', 1)
    page_obj=paginator.get_page(page_num)
    context = {
        'page_obj': page_obj,  # Pass book_reviews to the template
    }

    return render(request, 'home.html', context)
