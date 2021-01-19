from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class viewTest(TestCase):
    """A class which provides different methods to test the different views of the BAML site"""
    @classmethod
    def setUpTestData(cls):
        pass

    def test_page_is_not_found(self):
        response = self.client.get('/a_page_which_not_exists/')
        self.assertEqual(response.status_code, 404)

    def test_home_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_application_view_url_exists_at_desired_location(self):
        response = self.client.get('/application/')
        self.assertEqual(response.status_code, 200)

    def test_mentions_legales_view_url_exists_at_desired_location(self):
        response = self.client.get('/mention-legales/')
        self.assertEqual(response.status_code, 200)

    def test_plan_du_site_view_url_exists_at_desired_location4(self):
        response = self.client.get('/plan-du-site/')
        self.assertEqual(response.status_code, 200)

    def test_qui_sommes_nous_view_url_exists_at_desired_location5(self):
        response = self.client.get('/qui-sommes-nous/')
        self.assertEqual(response.status_code, 200)
###
###    def test_analyse_view_url_exists_at_desired_location6(self):
###        response = self.client.get('/analyze/')
###        self.assertEqual(response.status_code, 200)
###
###    def prediction_analyse_view_url_exists_at_desired_location7(self):
###        response = self.client.get('/prediction/')
###        self.assertEqual(response.status_code, 200)
