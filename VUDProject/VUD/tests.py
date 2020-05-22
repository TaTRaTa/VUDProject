from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from VUD.views import HomeView

# Create your tests here.
class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('vud:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/vud/')
        self.assertEquals(view.func.view_class, HomeView)

class CreateReqTests(TestCase):
    pass

class DetailReqTests(TestCase):
    pass

class EditReqTests(TestCase):
    pass

class SwitchReqTests(TestCase):
    pass
