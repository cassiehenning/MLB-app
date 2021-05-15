import statsapi
import pandas as pd
import numpy as np
import os
import json
from pprint import pprint
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
from datetime import date
from dotenv import load_dotenv
from app.email_service import send_email
from app import APP_ENV

load_dotenv

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

if APP_ENV == "development":
    lea = input("Please input a League code ")
    div = input("Please input a Division code ")
    lea = int(lea)
    div = int(div)
else:
    Lea = 104
    div = 204

def get_division_standings(league,division):
    standings = pd.DataFrame(statsapi.standings_data(league)[division]['teams'])
    standings = standings[['name','w','l']]
    df = pd.DataFrame(statsapi.standings_data(league)[division]['teams'])
    format_div_standings = df.to_html()
    print(format_div_standings)
    return standings
get_division_standings(lea,div) 

def get_player_ids(name):
    players = statsapi.lookup_player(name)
    player_ids = []
    for id_ in players:
        player_ids.append(id_['id'])
    return player_ids

if APP_ENV == "development":
    player = input("Please input a player full name to find hitting stats ")
    player = str(player)
else:
    player = 'Dansby Swanson'

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
    format_stats = dfr.to_html()    
    print(format_stats)  
get_stats_from_ids(player,'hitting')

if __name__ == "__main__":
    subject = "Your MLB update" #This tests to make sure the email capabilities are working correctly

    html = f""" 
    <body style="background-color:whitesmoke;">
    <h2 style="color: darkslateblue;">Hi, here are your MLB updates!</h3>
    <h4 style="color: grey;">Today's Date</h4>
    <p style="color: grey;">{date.today().strftime('%A, %B %d, %Y')}</p>
    <h2 style="color: darkslateblue;">Standings</h4>
        <p>{get_division_standings(lea,div)}</p>
    <h2 style="color: darkslateblue;">Hitting Stats</h4>
        <p>{get_stats_from_ids(player,'hitting')}</p>
    <h2 style="color: darkslateblue;">Have a good day!</h2>
    """

    send_email(subject, html)