from application import app
from flask import jsonify
import random

SpecialDict = {
    'Strength' : 1,
    'Perception' : 1,
    'Endurance' : 1,
    'Charisma' : 1,
    'Intelligence' : 1,
    'Agility' : 1,
    'Luck' : 1
    } #Default starting points

SpecialNameList = ['Strength','Perception','Endurance' ,'Charisma','Intelligence','Agility','Luck']
PointList = [1, 1, 1, 1, 1, 1, 1]
SpecialList = list(SpecialDict)

@app.route('/get-special', methods=['GET'])

def GenerateSpecial():
    for i in range(len(SpecialDict)):
        r = random.randrange(1,10)
        PointList[i] = r
        print('points list int', PointList) 
    if sum(PointList) == 40: #Highly unlikely   
        PrintSpecial(PointList)
    elif sum(PointList) > 40: 
        ChangeSpecial(PointList)
    elif sum(PointList) < 40:
        ChangeSpecial(PointList)

def ChangeSpecial(PointList):
    if sum(PointList) > 40: 
        for i in range(len(PointList)): 
            if sum(PointList) == 40:
                PrintSpecial(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =- 1
        PrintSpecial(PointList)
    elif sum(PointList) == 40: #if by some miracle the sum of the points is the max of the game the points will be printed out
        PrintSpecial(PointList)
    elif sum(PointList) < 40:
        for i in range(len(PointList)):
            if sum(PointList) == 40:
                PrintSpecial(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =+ 1
        PrintSpecial(PointList)
    
def PrintSpecial(PointList):
    for i in range(len(SpecialNameList)):
        SpecialDict[SpecialNameList[i]] = PointList[i]

def get_special():

    strength = SpecialDict["Strength"]

    perception = SpecialDict["Perception"]

    endurance = SpecialDict["Endurance"]

    charisma = SpecialDict["Charisma"]

    intelligence = SpecialDict["Intelligence"]
    
    agility = SpecialDict["Agility"]

    luck = SpecialDict["Luck"]

    return jsonify(strength=strength, perception=perception, endurance=endurance, charisma=charisma, intelligence=intelligence, agility=agility, luck=luck)