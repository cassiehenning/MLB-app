import statsapi
import pandas as pd
import numpy as np

print("------------------------------")
print("Hi! Welcome to the MLB app!")
print("------------------------------")
print("For reference, the codes for Leagues are as follows...")
print("American League is 103")
print("National League is 104")
print("------------------------------")
print("The codes for Divisions are as follows...")
print("American League West is 200")
print("American League East is 201")
print("American League Central is 202")
print("National League West 203")
print("National League East 204")
print("National League Central 205")
print("------------------------------")

lea = input("Please input a League code ")
div = input("Please input a Division code ")

def get_division_standings(league,division):
    standings = pd.DataFrame(statsapi.standings_data(league)[division]['teams'])
    standings = standings[['name','w','l']]
    df = pd.DataFrame(statsapi.standings_data(league)[division]['teams'])
    print(df)
    return standings
get_division_standings(104,204) #make this a user input

def get_player_ids(name):
    players = statsapi.lookup_player(name)
    player_ids = []
    for id_ in players:
        player_ids.append(id_['id'])
    return player_ids

player = input("Please input a player last name to find hitting stats ")

def get_stats_from_ids(name, stat_type):
    #get player IDs
    player_ids = get_player_ids(name)
    player_stats_list = []
    for player_id in player_ids:
        try:
            stats = statsapi.player_stat_data(player_id, group = stat_type)['stats'][0]['stats']
            stats.update({'player': statsapi.lookup_player(player_id)[0]['fullName']})
            player_stats_list.append(stats)
        except: 
            pass
    dfr = pd.DataFrame(player_stats_list)      
    print(dfr)  
get_stats_from_ids('Swanson','hitting') #make this a user input, probably only show hitting stats would be better