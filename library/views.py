from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.list import ListView
from library.models import Book, Author


class AWPUGListView(ListView):

    def get_context_data(*args, **kwargs):
        object_list = kwargs.get('object_list', [])
        return {'page_title': 'AWPUG Library', 
                'object_list':object_list}

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    output = '<h1>' + book.title + '</h1>'
    output += 'Page length: ' + str(book.page_length) + '</br>' 
                                    # remember page_length is an int
    if book.authors:
        output += 'Authors:'
        output += '<ul>'
        for author in book.authors.all():
            output += '<li>' + author.name + '</li>'
        output += '</ul>'

    return HttpResponse(output)

def request_details(request):
    user_agent = request.META['HTTP_USER_AGENT']

    output = '<p>Hi, user.</p>'
    output += '<p>The path you accessed is: ' + request.path + '</p>'
    output += '<p>The HTTP method you used is: ' + request.method + '</p>'
    user_agent = request.META['HTTP_USER_AGENT']
    output += 'Your user agent is: ' + user_agent + '</p>'


    output += '<p>Your POST data is:</p>'
    for key in request.POST:
        output += '<p>' + key + ': ' + request.POST[key]
    output += '<p>Your GET data is:</p>'
    for key in request.GET:
            output += '<p>' + key + ': ' + request.GET[key]

    return HttpResponse(output)

FORM_HTML = """
<html>
<head>
    <title>Add an author</title>
</head>
<body>
    <form action="%s" method="post">

        <input type="text" name="author_name">
        <input type="submit" value="Add author">
    </form>
</body>
</html>
"""
@csrf_exempt # ignore this until we talk about forms
def add_author(request):
    if request.method == 'GET':
        output = FORM_HTML % request.path
    else:
        a = Author(name=request.POST['author_name'])
        try:
            a.save()
        except Exception as e:
            output = "Whoops! There was an error: " + str(e)
        else:
            output = 'Success! We added an author named: ' + a.name

    return HttpResponse(output)

class AddAuthorView(View):
    def get(self, request):
        return HttpResponse(FORM_HTML % request.path)
    def post(self, request):
        a = Author(name=request.POST['author_name'])
        try:
            a.save()
        except Exception as e:
            output = "Whoops! There was an error: " + str(e)
        else:
            output = 'Success! We added an author named: ' + a.name
        return HttpResponse(output)
