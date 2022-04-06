from application import app
from flask import request, jsonify
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
        trait_2 == "None"
    elif trait_1 or trait_2 == 'Claustrophobia':
        strength = (strength + 1)
        perception = (perception + 1)
        endurance = (endurance + 1)
        charisma = (charisma + 1)
        intelligence = (intelligence + 1)
        agility = (agility + 1)
        luck = (luck + 1)
    elif trait_1 or trait_2 == 'Early_Bird':
        strength = (strength + 2)
        perception = (perception + 2)
        endurance = (endurance + 2)
        charisma = (charisma + 2)
        intelligence = (intelligence + 2)
        agility = (agility + 2)
        luck = (luck + 2)
    elif trait_1 or trait_2 == 'Four_Eyes':
        perception = (perception - 1)
    elif trait_1 or trait_2 == 'Small_Frame':
        agility = (agility + 1)

    if strength < 1:
        strength = 1
    elif strength > 10:
        strength = 10
    elif perception < 1:
        perception = 1
    elif perception > 10:
        perception = 10
    elif endurance < 1:
        endurance = 1
    elif endurance > 10:
        endurance = 10
    elif charisma < 1:
        charisma = 1
    elif charisma > 10:
        charisma = 10
    elif intelligence < 1:
        intelligence = 1
    elif intelligence > 10:
        intelligence = 10
    elif agility < 1:
        agility = 1
    elif agility > 10:
        agility = 10
    elif luck < 1:
        luck = 1
    elif luck > 10:
        luck = 10

    barter = (2 + (2*charisma) + ceil(luck/2))
    energy_weapons = (2 + (2*perception) + ceil(luck/2))
    explosives = (2 + (2*perception) + ceil(luck/2))
    guns = (2 + (2*agility) + ceil(luck/2))
    lockpick = (2 + (2*perception) + ceil(luck/2))
    medicine = (2 + (2*intelligence) + ceil(luck/2))
    melee_weapons = (2 + (2*strength) + ceil(luck/2))
    repair = (2 + (2*intelligence) + ceil(luck/2))
    science = (2 + (2*intelligence) + ceil(luck/2))
    sneak = (2 + (2*agility) + ceil(luck/2))
    speech = (2 + (2*charisma) + ceil(luck/2))
    survival = (2 + (2*endurance) + ceil(luck/2))
    unarmed = (2 + (2*endurance) + ceil(luck/2))
    
    if tag_1 or tag_2 or tag_3 == 'Barter':
        barter = (barter + 15)
    elif tag_1 or tag_2 or tag_3 == 'Energy_Weapons':
        energy_weapons = (energy_weapons + 15)
    elif tag_1 or tag_2 or tag_3 == 'Explosives':
        explosives = (explosives + 15)
    elif tag_1 or tag_2 or tag_3 == 'Guns':
        guns = (guns + 15)
    elif tag_1 or tag_2 or tag_3 == 'Lockpick':
        lockpick = (lockpick + 15)
    elif tag_1 or tag_2 or tag_3 == 'Medicine':
        medicine = (medicine + 15)
    elif tag_1 or tag_2 or tag_3 == 'Melee_Weapons':
        melee_weapons = (melee_weapons + 15)
    elif tag_1 or tag_2 or tag_3 == 'Repair':
        repair = (repair + 15)
    elif tag_1 or tag_2 or tag_3 == 'Science':
        science = (science + 15)
    elif tag_1 or tag_2 or tag_3 == 'Sneak':
        sneak = (sneak + 15)
    elif tag_1 or tag_2 or tag_3 == 'Speech':
        speech = (speech + 15)
    elif tag_1 or tag_2 or tag_3 == 'Survival':
        survival = (survival + 15)
    elif tag_1 or tag_2 or tag_3 == 'Unarmed':
        unarmed = (unarmed + 15)

    if trait_1 or trait_2 == 'Good_Natured' :
        barter = (barter + 5)
        medicine = (medicine + 5)
        repair = (repair + 5) 
        science = (science + 5)
        speech = (speech + 5)
        energy_weapons = (energy_weapons - 5)
        explosives = (explosives - 5)
        guns = (guns - 5)
        melee_weapons = (melee_weapons - 5)
    elif trait_1 or trait_2 == 'Skilled' :
        barter = (barter + 5)
        energy_weapons = (energy_weapons + 5)
        explosives = (explosives + 5)
        guns = (guns + 5)
        lockpick = (lockpick + 5)
        medicine = (medicine + 5)
        melee_weapons = (melee_weapons + 5)
        repair = (repair + 5)
        science = (science + 5)
        sneak = (sneak + 5)
        speech = (speech + 5)
        survival = (survival + 5)
        unarmed = (unarmed + 5)
    
    return jsonify(barter=barter, energy_weapons=energy_weapons, explosives = explosives, guns=guns, lockpick=lockpick, medicine=medicine, melee_weapons=melee_weapons,\
        repair=repair, science=science, sneak=sneak, speech=speech, survival=survival, unarmed=unarmed, trait_1 = trait_1, trait_2 = trait_2)