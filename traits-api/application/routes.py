from application import app
from flask import jsonify
from random import choice

traits = ['Built to Destory', 'Claustrophobia', 'Early Bird', 'Fast Shot', 'Four Eyes', 'Good Natured', 'Heavy Handed', 'Hoarder', 'Hot Blooded', 'Kamikaze', 'Logans Loophole', 'Loose Cannon'. 'Skilled', 'Small Frame', 'Trigger Discipline', 'Wild Wasteland'  ]

@app.route('/get-traits', methods=['GET'])
def get_trait():
    trait = choice(traits)
    return jsonify(trait=trait)