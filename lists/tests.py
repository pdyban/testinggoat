from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from .views import home_page
from django.template.loader import render_to_string


# Create your tests here.
class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        self.assertTrue(response.content.decode(), expected_html)
