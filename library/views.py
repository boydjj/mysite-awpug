from django.http import HttpResponse
from library.models import Book

def hello_world(request):
    return HttpResponse('Hi, AWPUG!')

def book_index(request):
    books = Book.objects.all()

    output = '<h1>Every book we know about:</h1>'
    output += '<ul>'
    for book in books:
        output += '<li>' + book.title + '</li>'
    output += '</ul>'

    return HttpResponse(output)
