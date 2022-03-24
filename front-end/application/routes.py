from application import app
from flask import Flask, request, render_template, url_for
import requests
from datetime import date



@app.route('/')
def index():
    special = requests.get('http://special-api:5000/get-special')
    traits = requests.get('http://traits-api:5000/get-traits')
    stats = requests.post('http://stats-api:5000/get-stats', json=dict(strength=special.json()['strength'], perception=special.json()['perception'], endurance=special.json()['endurance'], charisma=special.json()['charisma'], intelligence=special.json()['intelligence'], agility=special.json()['agility'], luck=special.json()['luck'], trait=traits.json()['trait'] ))