from application import app
from flask import jsonify
from random import choice

stats = ("Barter", "Energy_Weapons", "Explosives", "Guns", "Lockpick", "Medicine", "Melee_Weapons", "Repair", "Science", "Sneak", "Speech", "Survival", "Unarmed")

@app.route('/get_tags', methods=['GET'])
def get_tags():

    tag_1 = choice(stats)
    tag_2 = choice(stats)
    tag_3 = choice(stats)

    if tag_2 == tag_1 or tag_3:
        tag_2 = choice(stats)
    elif tag_3 == tag_1:
        tag_3 = choice(stats)

    return jsonify(tag_1=tag_1, tag_2=tag_2, tag_3=tag_3)