# API= Application programmimg Interface
#Api is data Pipeline between two Softweres
'''
Api is just a function (like function in python), but APi function is on server (i.e.- online) and with url data can be input from anywhere and 
get the output. 
The output from API is in JSON format (Java Script on Notation)
JSON is unoveversal data language

'''


'''
1. teams- {All teams played in IPL}
2. players- {All Player that played atleast one Match}
3. teams vs teams- {records between team}
4. team record-{input=one team, output- full record of team}
5. Batsman record- {overall record and record against each team}
6. Bowling record- {overall record and record against each team}



Deploy Online

'''

from flask import Flask
from flask import jsonify #easily convert dictionary to json file
import ipl #import  IPL.py file
from flask import request   # it will get input to function from url/form etc
from flask import json #to retun function data in json format 


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/api/teams")
def teams():
    teams =ipl.teamsAPI()   #calling teamAPI function from IPL.py file which is returning name of teams in the list format
    return jsonify(teams)   #here teams is easly converted in to dictionary

@app.route("/api/teamVteam")
def team_vs_team():
    team1=request.args.get('team1')
    #there is a specific formate of url to request data from url
    #request.args will fetch data from url and url will be in the form- http://127.0.0.1:5000/api/teamVteam?team1=Rajasthan%20Royals&team2=Royal%20Challengers%20Bangalore
    team2=request.args.get('team2')
    response= ipl.team_vs_team_API(team1,team2)
    return jsonify(response)

    




app.run(debug=True)


