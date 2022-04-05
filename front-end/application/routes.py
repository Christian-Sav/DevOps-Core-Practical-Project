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
    build = Build(barter = stats.json()["barter"], energy_weapons= stats.json()["energy_weapons"], explosives = stats.json()["explosives"], guns = stats.json()["guns"], \
        lockpick = stats.json()["lockpick"], medicine = stats.json()["medicine"], melee_weapons = stats.json()["melee_weapons"], repair = stats.json()["repair"], science = stats.json()["science"],\
        sneak = stats.json()["sneak"], speech = stats.json()["speech"], survival = stats.json()["survival"], unarmed = stats.json()["unarmed"], strength = special.json()["strength"], \
        perception = special.json()["perception"], endurance = special.json()["endurance"], charisma = special.json()["charisma"], intelligence = special.json()["intelligence"], \
        agility = special.json()["agility"], luck = special.json()["luck"], tag_1 = tags.json()["tag_1"], tag_2 = tags.json()["tag_2"], tag_3 = tags.json()["tag_3"], \
         trait_1 = stats.json()["trait_1"], trait_2 = stats.json()["trait_2"])
    db.session.add(build)
    db.session.commit
    return render_template('index.html', build = build)