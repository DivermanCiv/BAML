from django.test import TestCase
from django.urls import reverse
import unittest


# Create your tests here.
class indexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

# todo : prendre en compte la requête du formulaire
class applicationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

class mentionsLegalesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/mention-legales/')
        self.assertEqual(response.status_code, 200)

class planDuSiteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/plan-du-site/')
        self.assertEqual(response.status_code, 200)

class quiSommesNousViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/qui-sommes-nous/')
        self.assertEqual(response.status_code, 200)
