from application import app
from flask import request, jsonify
from math import ceil

@app.route('/get-stats', methods = ['POST'])
def stats():
    request_data = request.get_json()

    st_strength = request_data['strength']

    st_perception = request_data['perception']

    st_endurance = request_data['endurance']

    st_charisma = request_data['charisma']

    st_intelligence = request_data['intelligence']

    st_agility = request_data['agility']

    st_luck = request_data['luck']

    st_trait_1 = request_data['trait_1']

    st_trait_2 = request_data['trait_2']

    st_tag_1 = request_data['tag_1']

    st_tag_2 = request_data['tag_2']

    st_tag_3 = request_data['tag_3']

    #establishing all json variables

    if st_trait_1 == st_trait_2:
        st_trait_2 == "None"
    elif st_trait_1 or st_trait_2 == 'Claustrophobia':
        st_strength = (st_strength + 1)
        st_perception = (st_perception + 1)
        st_endurance = (st_endurance + 1)
        st_charisma = (st_charisma + 1)
        st_intelligence = (st_intelligence + 1)
        st_agility = (st_agility + 1)
        st_luck = (st_luck + 1)
    elif st_trait_1 or st_trait_2 == 'Early_Bird':
        st_strength = (st_strength + 2)
        st_perception = (st_perception + 2)
        st_endurance = (st_endurance + 2)
        st_charisma = (st_charisma + 2)
        st_intelligence = (st_intelligence + 2)
        st_agility = (st_agility+ 2)
        st_luck = (st_luck + 2)
    elif st_trait_1 or st_trait_2 == 'Four_Eyes':
        st_perception = (st_perception - 1)
    elif st_trait_1 or st_trait_2 == 'Small_Frame':
        st_agility = (st_agility + 1)

# establashing affects of triats

    if st_strength < 1:
        st_strength = 1
    elif st_strength > 10:
        st_strength = 10
    elif st_perception < 1:
        st_perception = 1
    elif st_perception > 10:
        st_perception = 10
    elif st_endurance < 1:
        st_endurance = 1
    elif st_endurance > 10:
        st_endurance = 10
    elif st_charisma < 1:
        st_charisma = 1
    elif st_charisma > 10:
        st_charisma = 10
    elif st_intelligence < 1:
        st_intelligence = 1
    elif st_intelligence > 10:
        st_intelligence = 10
    elif st_agility < 1:
        st_agility = 1
    elif st_agility > 10:
        st_agility = 10
    elif st_luck < 1:
        st_luck = 1
    elif st_luck > 10:
        st_luck = 10

# ensuring specials are between 1 and 10

    barter = (2 + (2*st_charisma) + ceil(st_luck/2))
    energy_weapons = (2 + (2*st_perception) + ceil(st_luck/2))
    explosives = (2 + (2*st_perception) + ceil(st_luck/2))
    guns = (2 + (2*st_agility) + ceil(st_luck/2))
    lockpick = (2 + (2*st_perception) + ceil(st_luck/2))
    medicine = (2 + (2*st_intelligence) + ceil(st_luck/2))
    melee_weapons = (2 + (2*st_strength) + ceil(st_luck/2))
    repair = (2 + (2*st_intelligence) + ceil(st_luck/2))
    science = (2 + (2*st_intelligence) + ceil(st_luck/2))
    sneak = (2 + (2*st_agility) + ceil(st_luck/2))
    speech = (2 + (2*st_charisma) + ceil(st_luck/2))
    survival = (2 + (2*st_endurance) + ceil(st_luck/2))
    unarmed = (2 + (2*st_endurance) + ceil(st_luck/2))
    
#calculating stats

    if st_tag_1 or st_tag_2 or st_tag_3 == 'Barter':
        barter = (barter + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Energy_Weapons':
        energy_weapons = (energy_weapons + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Explosives':
        explosives = (explosives + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Guns':
        guns = (guns + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Lockpick':
        lockpick = (lockpick + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Medicine':
        medicine = (medicine + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Melee_Weapons':
        melee_weapons = (melee_weapons + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Repair':
        repair = (repair + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Science':
        science = (science + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Sneak':
        sneak = (sneak + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Speech':
        speech = (speech + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Survival':
        survival = (survival + 15)
    elif st_tag_1 or st_tag_2 or st_tag_3 == 'Unarmed':
        unarmed = (unarmed + 15)

# adding traits to stats

    if st_trait_1 or st_trait_2 == 'Good_Natured' :
        barter = (barter + 5)
        medicine = (medicine + 5)
        repair = (repair + 5) 
        science = (science + 5)
        speech = (speech + 5)
        energy_weapons = (energy_weapons - 5)
        explosives = (explosives - 5)
        guns = (guns - 5)
        melee_weapons = (melee_weapons - 5)
    elif st_trait_1 or st_trait_2 == 'Skilled' :
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

    # adding traits to stats
    
    return jsonify(barter=barter, energy_weapons=energy_weapons, explosives = explosives, guns=guns, lockpick=lockpick, medicine=medicine, melee_weapons=melee_weapons,\
        repair=repair, science=science, sneak=sneak, speech=speech, survival=survival, unarmed=unarmed, trait_1=st_trait_1, trait_2=st_trait_2)