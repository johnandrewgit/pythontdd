from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Personal note: our tests inherit from TestCase, a specialized
# unit testing tool courtesy of Django

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)