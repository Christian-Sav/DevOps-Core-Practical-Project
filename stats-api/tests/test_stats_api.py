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
        json={"strength":1, "perception":1, "endurance":1, "charisma":1, "intelligence":1, "agility":1, "luck":1, "trait_1":"Heavy_Handed",\
         "trait_2":"Hot_Blooded", "tag_1":"Barter", "tag_2":"Energy_Weapons", "tag_3":"Explosives"})
        self.assert200(response)
        self.assertIn(b'{"barter":20, energy_weapons:20, explosives:20, guns:5, lockpick:5, medicine:5, melee_Weapons:5, repair:5, science:5, sneak:5, speech:5, survival:5, unarmed:5, trait_1="Heavy_Handed", trait_2="Hot_Blooded"}', response.data)
        
