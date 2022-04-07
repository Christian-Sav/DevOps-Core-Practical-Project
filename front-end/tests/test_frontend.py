from application import app, db
from application.models import Build
from flask import url_for
import requests_mock
from flask_testing import TestCase
from datetime import datetime

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app

class TestView(TestBase):
    def setUp(self):
        sample_result = Build(strength = 1, perception = 1, endurance = 1, charisma = 1, intelligence = 1, agility = 1, luck = 1, tag_1 = 'Barter', \
            tag_2 = 'Energy_Weapons', tag_3 = 'Explosives', trait_1 = 'Heavy_Handed', trait_2 = 'Hot_Blooded', barter= 20, energy_weapons=20, explosives = 20, \
            guns=5, lockpick=5, medicine=5, melee_weapons=5, repair=5, science=5, sneak=5, speech=5, survival=5, unarmed=5)
        db.create_all()
        db.session.add(sample_result)
        db.session.commit

    def tearDown(self):
        db.session.remove()
        db.drop_all

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://special-api:5000/get-special', json={"strength":1, "perception":1, "endurance":1, "charisma":1, "intelligence":1, "agility":1, "luck":1})
            m.get('http://traits-api:5000/get-traits', json={"trait_1":'Heavy_Handed', "trait_2":'Hot_Blooded'})
            m.get('http://tags-api:5000/get-tags', json={"tag_1":'Guns', "tag_2":'Lockpick', "tag_3":'Medicine'})
            m.post('http://stats-api:5000/get-stats', json={"Barter":5, "energy_weapons":5, "explosives":5, \
                "guns":20, "lockpick":20, "medicine":20, "melee_weapons":5, "repair":5, "science":5, "sneak":5, "speech":5, "survival":5, "unarmed":5})
            response = self.client.get(url_for('index'))
            self.assertIn(b'In This build your special skills are: \n Strength: 1} \n Perception: 1 \n Endurance: 1 \
                \n Charisma: 1 \n Intelligence: 1 \n Agility: 1 \n Luck: 1 \n Your Tagged Skills are: Guns, \
                Lockpick and Medicine \n Your Traits are: Heavy Handed and Hot Blooded \n And your skill totals are: \n Barter: 5 \
                \n Energy Weapons: 5 \n Explosives: 5 \n Guns: 20 \n Lockpick: 20 \n Medicine: 20 \
                \n Melee Weapons: 5 \n Repair: 5 \n Science: 5 \n Sneak: 5 \n Speech: 5 \n Survival: 5 \n Unarmed: 5 \n I hope you enjoy this build!', response.data)
            self.assertNotIn(b"_")