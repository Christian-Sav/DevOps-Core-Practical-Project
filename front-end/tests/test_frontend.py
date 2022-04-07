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
        sample_result = Build(id = 1, strength = 1, perception = 1, endurance = 1, charisma = 1, intelligence = 1, agility = 1, luck = 1, tag_1 = 'Barter', \
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
            m.post('http://stats-api:5000/get-stats', json={"barter":5, "energy_weapons":5, "explosives":5, "guns":20, "lockpick":20, "medicine":20, "melee_weapons":5, "repair":5, "science":5, "sneak":5, "speech":5, "survival":5, "unarmed":5, "trait_1":'Heavy_Handed', "trait_2":'Hot_Blooded'})
            response = self.client.get(url_for('index'))
            self.assertIn(b'<html>\n<body style="background-color: rgb(46, 49, 46); font-family: Monofonto">\n<h1 style="color: rgb(255,182,65); text-align:center">Fallout: New Vegas Random Character Generator </h1>\n<h2 style="color: rgb(255,182,65); text-align:center">|| <a style="color: rgb(255,182,65)" href="/">Home</a> ||\n\n<h1 style="color: rgb(255,182,65)"> This Build: </h1>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" >In This build your special skills are: </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Strength: 1 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Perception: 1 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Endurance: 1</p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Charisma: 1 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Intelligence: 1             </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Agility: 1 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Luck: 1 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Your Tagged Skills are: Guns, Lockpick and Medicine             </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Your Traits are: Heavy Handed and Hot Blooded </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > And your skill totals are: </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Barter: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Energy Weapons: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Explosives: 5             </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Guns: 20 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Lockpick: 20 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Medicine: 20 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Melee Weapons: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Repair: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Science: 5             </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Sneak: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Speech: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Survival: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > Unarmed: 5 </p>\n<br>\n\n<p style="color: rgb(255,182,65); font: size 18px;" > I hope you enjoy this build!</p>\n<br>\n\n\n</body>\n</html>', response.data)
            self.assertNotIn(b"_", response.data)