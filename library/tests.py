import django

import pytest
import mock

import views


class TestRequestDetails(object):
    def test_request_details(self):
        request = django.http.HttpRequest()
        request.META['HTTP_USER_AGENT'] = 'tester'
        request.method = 'GET'
        resp = views.request_details(request)
        assert resp.status_code == 200
        assert resp.content.startswith('<p>')
        assert resp.content.endswith('</p>')


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

        # Reset in case we want to use that view reasonably again.
        views.get_object_or_404 = old_get_object_or_404
