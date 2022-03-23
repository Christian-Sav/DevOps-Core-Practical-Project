from application import app
from flask import Flask, request, Response
import random

@app.route('/get_strength', methods=['GET'])
def name():
    strength = random.randint(0,11)
    return Response(strength, mimetype='text/plain')

@app.route('/get_endurance', methods=['GET'])
def name():
    endurance = random.randint(0,11)
    return Response(endurance, mimetype='text/plain')

@app.route('/get_charisma', methods=['GET'])
def name():
    charisma = random.randint(0,11)
    return Response(charisma, mimetype='text/plain')

@app.route('/get_intelligence', methods=['GET'])
def name():
    intelligence = random.randint(0,11)
    return Response(intelligence, mimetype='text/plain')

@app.route('/get_agility', methods=['GET'])
def name():
    agility = random.randint(0,11)
    return Response(agility, mimetype='text/plain')

@app.route('/get_luck', methods=['GET'])
def name():
    luck = random.randint(0,11)
    return Response(luck, mimetype='text/plain')