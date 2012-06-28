import django

import pytest
import mock
from library.models import Book

import views


class TestRequestDetails(object):
    def test_request_details(self):
        request = django.http.HttpRequest()
        request.META['HTTP_USER_AGENT'] = 'tester'
        request.method = 'GET'
        response = views.request_details(request)
        assert response.status_code == 200
        assert response.content.startswith('<p>')
        assert response.content.endswith('</p>')


class TestBookDetail(object):
    def test_book_detail_not_found(self):
        request = django.http.HttpRequest()
        test_book_id = 1

        # Keep a handle on the original get_object_or_404
        old_get_object_or_404 = views.get_object_or_404

        # Replace get_object_or_404 with a mock object.
        mock_get_object_or_404 = mock.Mock(side_effect=django.http.Http404('book not found'))
        views.get_object_or_404 = mock_get_object_or_404

        with pytest.raises(django.http.Http404):
            response = views.book_detail(request, test_book_id)

        # Reset in case we want to use the real function again.
        views.get_object_or_404 = old_get_object_or_404


    def test_book_detail_found(self):
        request = django.http.HttpRequest()
        test_book_id = 1000
        test_book_result = Book(id=test_book_id, title='All I know about Mock', page_length=2)

        # This time, we'll use patch to handle keeping track of the original get_object_or_404.
        with mock.patch('library.views.get_object_or_404') as mock_get_object_or_404:
            mock_get_object_or_404.return_value = test_book_result
            response = views.book_detail(request, test_book_id)
            mock_get_object_or_404.assert_called_with(Book, id=test_book_id)

        assert response.content.startswith('<h1>')
        assert response.content.endswith('</br>')
