from django.http import response
from django.test import TestCase , SimpleTestCase
from django.urls import reverse


# Create your tests here.
class snacks_tests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'about.html')
        self.assertTemplateUsed(response,'base.html')