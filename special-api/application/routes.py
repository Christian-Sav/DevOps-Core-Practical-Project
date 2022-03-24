from application import app
from flask import Flask, request, jsonify
import random
    
@app.route('/get-special', methods=['GET'])
def get_special():

    strength = random.randint(1,10)

    perception = random.randint(1,10)

    endurance = random.randint(1,10)

    charisma = random.randint(1,10)

    intelligence = random.randint(1,10)
    
    agility = random.randint(1,10)

    luck = random.randint(1,10)

    return jsonify(strength=strength, perception=perception, endurance=endurance, charisma=charisma, intelligence=intelligence, agility=agility, luck=luck)