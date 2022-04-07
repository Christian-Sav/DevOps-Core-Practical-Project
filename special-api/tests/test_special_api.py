from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):

    def test_get_special(self):
       with patch('application.routes.randint') as r:
           r.return_value = 2
           response = self.client.get(url_for('get_special'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'agility:2', response.data)