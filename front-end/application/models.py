from application import db

class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    endurance = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    luck = db.Column(db.Integer),
    tag_1 = db.Column(db.String(20)),
    tag_2 = db.Column(db.String(20)),
    tag_3 = db.Column(db.String(20)),
    trait_1 = db.Column(db.String(20)),
    trait_2 = db.Column(db.String(20)),
    barter = db.Column(db.Integer)
    energy_weapons = db.Column(db.Integer)
    explosives = db.Column(db.Integer)
    guns = db.Column(db.Integer)
    lockpick = db.Column(db.Integer)
    medicine = db.Column(db.Integer)
    melee_weapons = db.Column(db.Integer)
    repair = db.Column(db.Integer)
    science = db.Column(db.Integer)
    sneak = db.Column(db.Integer)
    speech = db.Column(db.Integer)
    survival = db.Column(db.Integer)
    unarmed = db.Column(db.Integer)
