from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.decorators.csrf import csrf_exempt
from library.models import Author, Book
from library.views import AddAuthorView, AWPUGListView

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', TemplateView.as_view(
                template_name="library/index.html", 
                get_context_data=lambda:{'page_title':"AWPUG Library"})),
    url(r'^books/(\d+)/$', 'library.views.book_detail'),
    url(r'^request_details/$', 'library.views.request_details'),
    url(r'^add_author/$', 'library.views.add_author'),
    url(r'^books/$', AWPUGListView.as_view(model=Book), 
                             name='library.views.book_index'),
    url(r'^authors/$', AWPUGListView.as_view(model=Author), 
                             name='library.views.authors'),
    url(r'^add_author_class/$', csrf_exempt(AddAuthorView.as_view())),
)
