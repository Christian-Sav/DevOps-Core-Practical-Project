from application import app
from flask import jsonify
from random import sample

stats = set(["barter", "energy_weapons", "explosives", "guns", "lockpick", "medicine", "melee", "repair", "science", "sneak", "speech", "survival", "unarmed"])
stats_2  = sample(list(stats), 3)

@app.route('/get-tags', methods=['GET'])
def get_tags():
    tag_1 = stats_2[0]
    tag_2 = stats_2[1]
    tag_3 = stats_2[2]
    return jsonify(tag_1=tag_1, tag_2=tag_2, tag_3=tag_3)