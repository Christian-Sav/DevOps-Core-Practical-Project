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
        self.assertIn(b'{"barter":45,"energy_weapons":20,"explosives":20,"guns":12,"lockpick":25,"medicine":14,"melee_weapons":16,"repair":14,"science":14,"sneak":17,"speech":30,"survival":13,"trait_1":"Heavy_Handed","trait_2":"Hot_Blooded","unarmed":13}\n', response.data)
