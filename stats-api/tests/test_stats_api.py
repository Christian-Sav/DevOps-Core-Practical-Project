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
    def test_get_stats(self):
        response = self.client.post(url_for('stats'),
        json={"strength":1, "perception":1, "endurance":1, "charisma":1, "intelligence":1, "agility":1, "luck":1, "trait_1":"Heavy_Handed", "trait_2":"Hot_Blooded", \
        "tag_1":"Explosives", "tag_2":"Unarmed", "tag_3":"Lockpick"})
        self.assert200(response)
        self.assertIn(b'{"barter":5', response.data)

class TestViews(TestBase):
    def test_tags(self):
        response = self.client.post(url_for('stats'),
        json={"strength":1, "perception":1, "endurance":1, "charisma":1, "intelligence":1, "agility":1, "luck":1, "st_trait_1":"Heavy_Handed", "st_trait_2":"Hot_Blooded", \
        "st_tag_1":"Barter", "st_tag_2":"Energy_Weapons", "tag_3":"Explosives"})
        self.assert200(response)
        self.assertIn(b'{"barter":20', response.data)
        self.assertIn(b'{"Energy_Weapons":20', response.data)
        self.assertIn(b'{"Explosives":20', response.data)
