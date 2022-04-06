from application import app
from flask import jsonify
import random




@app.route('/get-special', methods=['GET'])

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

def GenerateSpecial():
    for i in range(len(SpecialDict)):
        print('i = ' + str(i)) #DEBUG
        r = random.randrange(1,10)
        print(r) #DEBUG
        PointList[i] = r
        print('points list int', PointList) #DEBUG
    if sum(PointList) == 40: #Highly unlikely   
        PrintSpecial(PointList)
    elif sum(PointList) > 40: #bigger than
        ChangeSpecial(PointList)
    elif sum(PointList) < 40:
        ChangeSpecial(PointList)
    else:
        return("Unknown Error")

def ChangeSpecial(PointList): #changes the points if there are to many
    print('On ChangeSpecial()') #DEBUG
    if sum(PointList) > 40: #chceks to see if the sum of the points is bigger than the max points for the game
        print('On if sum > game')
        for i in range(len(PointList)): #might have to redo all of this 
            if sum(PointList) == 40:
                PrintSpecial(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =- 1
            else:
                return("Unknown Error")
        PrintSpecial(PointList)
    elif sum(PointList) == 40: #if by some miracle the sum of the points is the max of the game the points will be printed out
        PrintSpecial(PointList)
    elif sum(PointList) < 40: #checks to see if the sum of the points is smaller than the max points for the game
        for i in range(len(PointList)): #might have to redo all of this 
            if sum(PointList) == 40:
                PrintSpecial(PointList)
            elif PointList[i] == 1:
                continue
            elif PointList[i] > 1:
                PointList[i] =+ 1
            else:
                return("Unknown Error")
        PrintSpecial(PointList)
    else:
        return("Unknown Error")
    
def PrintSpecial(PointsList):
    print('Points Used: ' + str(sum(PointsList)))
    for i in range(len(SpecialNameList)):
        SpecialDict[SpecialNameList[i]] = PointList[i]
        print(SpecialNameList[i] + ': ' + str(SpecialDict[SpecialNameList[i]]))
        
def get_special():

    strength = SpecialDict["Strength"]

    perception = SpecialDict["Perception"]

    endurance = SpecialDict["Endurance"]

    charisma = SpecialDict["Charisma"]

    intelligence = SpecialDict["Intelligence"]
    
    agility = SpecialDict["Agility"]

    luck = SpecialDict["Luck"]

    return jsonify(strength=strength, perception=perception, endurance=endurance, charisma=charisma, intelligence=intelligence, agility=agility, luck=luck)