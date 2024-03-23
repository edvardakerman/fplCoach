import sys
import requests
import os
from dotenv import load_dotenv
import handleLocalData

##from forward import Forward

load_dotenv()

API_KEY = os.getenv('RAPDI_API_KEY')

import requests

base_url = 'https://fantasy.premierleague.com/api/'

handleLocalData = handleLocalData.HandleLocalData()


def fetchData():
    return requests.get(base_url+'bootstrap-static/').json()

def storeData():
    defenders = []
    midfielders = []
    goalkeepers = []
    forwards = []
    for p in fetchData()['elements']:
        match p['element_type']:
            case 1:
                goalkeepers.append(p)
            case 2:
                defenders.append(p)
            case 3:
                midfielders.append(p)
            case 4:
                forwards.append(p)

    handleLocalData.saveData(goalkeepers, 0)
    handleLocalData.saveData(defenders, 1)
    handleLocalData.saveData(midfielders, 2)
    handleLocalData.saveData(forwards, 3)
            
        

# players.sort(key=lambda x: float(x['form']), reverse=True)

def getSpace(name):
    return " " * (17 - len(name))

def getSpaceInt(num):
    if num < 10 and num >= 0:
        return "  "
    elif num < 100:
        return " "
    else:
        return ""

def getSpaceFloat(num):
    if num < 10 and num >= 0:
        return " "
    else:
        return ""

def sortPlayers(players):
    match sys.argv[3]:
        case "form":
            players.sort(key=lambda x: float(x['form']), reverse=True)
        case "points":
            players.sort(key=lambda x: float(x['total_points']), reverse=True)
        case "threat":
            players.sort(key=lambda x: float(x['threat']), reverse=True)
        case "goals":
            players.sort(key=lambda x: float(x['goals_scored']), reverse=True)
        case "assists":
            players.sort(key=lambda x: float(x['assists']), reverse=True)
    return players

def printPlayers(pos):
    players = sortPlayers(handleLocalData.loadData(pos))
    print("Name              | Form | Pts | Gs  | Ass | Threat")
    for p in players:
        print("-------------------------------------------------")
        print(p['web_name'] + getSpace(p['web_name']) + " | " + str(p['form']) + getSpaceFloat(float(p['form'])) + " | " + str(p['total_points']) + getSpaceInt(p['total_points']) + " | " + str(p['goals_scored']) + getSpaceInt(p['goals_scored'])  + " | " + str(p['assists']) + getSpaceInt(p['assists']) + " | " + str(p['threat']))
        


if sys.argv[1] == 'fetch':
    storeData()
elif sys.argv[1] == 'print':
    if sys.argv[2] == 'gk':
        printPlayers(0)
    elif sys.argv[2] == 'def':
        printPlayers(1)
    elif sys.argv[2] == 'mid':
        printPlayers(2)
    elif sys.argv[2] == 'fwd':
        printPlayers(3)
    else:
        printPlayers(0)

    
    # if float(i['form']) > 7:
    #     print(i['web_name'] + ", " + str(i['form']))
##print('Number of events:', len(odds_json))