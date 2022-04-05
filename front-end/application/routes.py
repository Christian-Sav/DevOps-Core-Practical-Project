from application import app, db
from flask import render_template
from application.models import Build
import requests

@app.route('/', methods = ['GET'])
def index():
    special = requests.get('http://special-api:5000/get-special')
    traits = requests.get('http://traits-api:5000/get-traits')
    tags = requests.get('http://tags-api:5000/get-tags')
    stats = requests.post('http://stats-api:5000/get-stats', json=dict(strength=special.json()["strength"], perception=special.json()["perception"], endurance=special.json()["endurance"], \
         charisma=special.json()["charisma"], intelligence=special.json()["intelligence"], agility=special.json()["agility"], \
         luck=special.json()["luck"], trait_1=traits.json()["trait_1"], trait_2=traits.json()["trait_2"], tag_1=tags.json()["tag_1"], tag_2=tags.json()["tag_2"], tag_3=tags.json()["tag_3"] ))
    build = Build(barter = stats.barter, energy_weapons= stats.energy_weapons, explosives = stats.explosives, guns = stats.guns, lockpick = stats.lockpick, medicine = stats.medicine, \
        melee = stats.melee, repair = stats.repair, science = stats.science, sneak = stats.sneak, speech = stats.speech, survival = stats.survival, unarmed = stats.unarmed, \
        strength = stats.strength, perception = stats.perception, endurance = stats.endurance, charisma = stats.charisma, intelligence = stats.intelligence, agility = stats.agility, \
        luck = stats.luck, tag_1 = tags.tag_1, tag_2 = tags.tag_2, tag_3 = tags.tag_3, trait_1 = traits.trait_1, trait_2 = traits.trait_2)
    db.session.add(build)
    db.session.commit
    return render_template('index.html', build = build)