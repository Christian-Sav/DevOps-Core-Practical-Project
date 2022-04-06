from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
# import the app's classes and objects
from application import app

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_trait_1(self):
        with patch('application.routes.choice') as r:
            r.return_value = 'Claustrophobia'
            response = self.client.get(url_for('get_trait'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Claustrophobia', response.data)
