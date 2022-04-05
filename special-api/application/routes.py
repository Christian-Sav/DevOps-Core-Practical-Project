from application import app
from flask import jsonify
from random import randint
    
@app.route('/get-special', methods=['GET'])
def get_special():

    strength = randint(1,10)

    perception = randint(1,10)

    endurance = randint(1,10)

    charisma = randint(1,10)

    intelligence = randint(1,10)
    
    agility = randint(1,10)

    luck = randint(1,10)

    return jsonify(strength=strength, perception=perception, endurance=endurance, charisma=charisma, intelligence=intelligence, agility=agility, luck=luck)