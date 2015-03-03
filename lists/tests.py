from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Personal note: our tests inherit from TestCase, a specialized
# unit testing tool courtesy of Django

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')

        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        # note groupings

        # Setup (the test)
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        # Exercise (function call)
        response = home_page(request)

        # Assert
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)

        # SELF SUMMARY (before expected_html part)
        # not sure about the request = HttpRequest() but it's set up
        # method attribute set to 'POST' -- i believe the HttpRequest()
        #   function call likely has, literally, the HTTP request info
        # and the dictionary contains the 'item_text' key requested by the client,
        #   which is then set to 'A new list item'
        # the response is sent to a view called with our request info
        # then we see if our expected item_text description is found in
        #   the response.content (decoded for Python3)