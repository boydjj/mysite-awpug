from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    output = '<h1>' + book.title + '</h1>'
    output += 'Page length: ' + str(book.page_length) + '</br>' # remember page_length is an int
    if book.authors:
        output += 'Authors:'
        output += '<ul>'
        for author in book.authors.all():
            output += '<li>' + author.name + '</li>'
        output += '</ul>'

    return HttpResponse(output)
