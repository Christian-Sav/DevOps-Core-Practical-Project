from application import db

class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    endurance = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    luck = db.Column(db.Integer)
    tag_1 = db.Column(db.String(20))
    tag_2 = db.Column(db.String(20))
    tag_3 = db.Column(db.String(20))
    trait_1 = db.Column(db.String(20))
    trait_2 = db.Column(db.String(20))
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
    def __str__(self):
        build_full = f"In This build your special skills are: \n Strength of: {self.strength} \n Perception of: {self.perception} \n Endurance of: {self.endurance}\n Charisma of: {self.charisma} \n Intelligence of: {self.intelligence} \
            \n Agility of: {self.agility} \n Luck of: {self.luck} \n Your Tagged Skills are: {self.tag_1}, {self.tag_2} and {self.tag_3} \
            \n Your Traits are: {self.trait_1} and {self.trait_2} \n And your skill totals are: \n Barter: {self.barter} \n Energy Weapons: {self.energy_weapons} \n Explosives: {self.explosives} \
            \n Guns: {self.guns} \n Lockpick: {self.lockpick} \n Medicine: {self.medicine} \n Melee Weapons: {self.melee_weapons} \n Repair: {self.repair} \n Science: {self.science} \
            \n Sneak: {self.sneak} \n Speech: {self.speech} \n Survival: {self.survival} \n Unarmed: {self.unarmed} \n I hope you enjoy this build!"
        return build_full.replace('\n', ' ')
