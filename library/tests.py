import django

import views


class TestRequestDetails(object):
    def test_request_details(self):
        req = django.http.HttpRequest()
        req.META['HTTP_USER_AGENT'] = 'tester'
        req.method = 'GET'
        resp = views.request_details(req)
        assert resp.status_code == 200
        assert resp.content.startswith('<p>')
        assert resp.content.endswith('</p>')


