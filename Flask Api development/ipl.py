import pandas as pd
import numpy as np

matches= pd.read_csv(r"A:\Work Docs\DATA Set\ipl-matches.csv")

def teamsAPI():
    teams= list(set(list(matches['Team1']) +list(matches['Team2'])))
    
    teams_dic = {"teams":teams}     # making a dictionary with key=teams and values = list of teams
    return teams_dic


def team_vs_team_API(team1,team2):

    valid_team=list(set(list(matches['Team1']) +list(matches['Team2'])))

    if team1 in valid_team and team2 in team2 in valid_team:     
        temp_df=matches[((matches['Team1']==team1)&(matches['Team2']==team2))|((matches['Team1']==team2)&(matches['Team2']==team1))]
        total_matches=temp_df.shape[0]
        matches_won_team1=temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2=temp_df['WinningTeam'].value_counts()[team2]
        draws=total_matches-matches_won_team1-matches_won_team2
        #making a dictionary with name= response to return information through dictionary
        response={
                        "total_matches":str(total_matches),
                        team1:str(matches_won_team1),
                        team2:str(matches_won_team2),
                        "draw":str(draws)
                }
        return response 
    else:
        return {"message":"invalid team name"}
    


    