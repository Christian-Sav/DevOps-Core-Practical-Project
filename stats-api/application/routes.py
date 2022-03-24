from application import app
from flask import Flask, jsonify, request
from math import ceil

@app.route('/get-stats', methods = ['POST'])
def stats():
    request_data = request.get_json()
    strength = request_data['strength']
    perception = request_data['perception']
    endurance = request_data['endurance']
    charisma = request_data['charisma']
    intelligence = request_data['intelligence']
    agility = request_data['agility']
    luck = request_data['luck']
    trait_1 = request_data['trait_1']
    trait_2 = request_data['trait_2']
    tag_1 = request_data['tag_1']
    tag_2 = request_data['tag_2']
    tag_3 = request_data['tag_3']

    if trait_1 == trait_2:
        trait_2 == 'None'
    elif trait_1 or trait_2 == Claustrophobia:
        strength = (strength + 1), perception = (perception + 1), endurance = (endurance + 1), charisma = (charisma + 1), intelligence = (intelligence + 1), agility = (agility + 1), luck = (luck + 1)
    elif trait_1 or trait_2 == Early_Bird:
        strength = (strength + 2), perception = (perception + 2), endurance = (endurance + 2), charisma = (charisma + 2), intelligence = (intelligence + 2), agility = (agility + 2), luck = (luck + 2)
    elif trait_1 or trait_2 == Four_Eyes:
        perception = (perception - 1)
    elif trait_1 or trait_2 = Small_Frame:
        agility = (agility + 1)

    barter = (2 + (2*charisma) + ceil.(luck/2))
    energy_weapons = (2 + (2*perception) + ceil.(luck/2))
    explosives = (2 + (2*perception) + ceil.(luck/2))
    guns = (2 + (2*agility) + ceil.(luck/2))
    lockpick = (2 + (2*perception) + ceil.(luck/2))
    medicine = (2 + (2*intelligence) + ceil.(luck/2))
    melee = (2 + (2*strength) + ceil.(luck/2))
    repair = (2 + (2*intelligence) + ceil.(luck/2))
    science = (2 + (2*intelligence) + ceil.(luck/2))
    sneak = (2 + (2*agility) + ceil.(luck/2))
    speech = (2 + (2*charisma) + ceil.(luck/2))
    survival = (2 + (2*endurance) + ceil.(luck/2))
    unarmed = (2 + (2*endurance) + ceil.(luck/2))