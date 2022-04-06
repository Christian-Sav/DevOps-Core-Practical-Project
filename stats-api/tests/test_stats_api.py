from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):
    def test_get_stast(self):
        response = self.client.post(url_for('stats'),
        json={"strength":7, "perception":10, "endurance":3, "charisma":9, "intelligence":1, "agility":5, "luck":5, "trait_1":"Heavy_Handed", "trait_2":"Hot_Blooded", \
        "tag_1":"Explosives", "tag_2":"Unarmed", "tag_3":"Lockpick"})
        self.assert200(response)
        self.assertIn(b'{"barter":45', response.data)
