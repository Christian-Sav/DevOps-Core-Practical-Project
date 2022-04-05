from application import app
from flask import jsonify
from random import choice

traits = ['Built_to_Destory', 'Claustrophobia', 'Early_Bird', 'Fast_Shot', 'Four_Eyes', 'Good_Natured', 'Heavy_Handed', 'Hoarder', 'Hot_Blooded', 'Kamikaze', 'Logans_Loophole', 'Loose_Cannon', 'Skilled', 'Small_Frame', 'Trigger_Discipline', 'Wild_Wasteland'  ]

@app.route('/get-traits', methods=['GET'])
def get_trait():
    trait_1 = choice(traits)
    trait_2 = choice(traits)
    return jsonify(trait_1=trait_1, trait_2=trait_2)