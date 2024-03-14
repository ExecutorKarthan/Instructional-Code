import random

class Team:
    def __init__(self, teams_played, wins, losses, skill, name):
        self.teams_played = teams_played
        self.wins = wins
        self.losses = losses
        self.skill = skill  
        self.name = name
        
    def __init__(self, teams_played, wins, losses, skill):
        self.teams_played = teams_played
        self.wins = wins
        self.losses = losses
        self.skill = skill  
    
def bracket(original_bracket):
    games_played = 0
    temp_win = []
    temp_lose = []
    while (len(original_bracket) > 1):
        high = original_bracket.pop()
        low = original_bracket.pop(0)
        #print(high.name, "vs", low.name)
        if(high.skill > low.skill):
            high.wins = high.wins + 1
            low.losses = low.losses + 1
            #high.teams_played.append(low.name)
            #low.teams_played.append(high.name)
            temp_win.append(high)
            temp_lose.append(low)
        else:
            low.wins = low.wins + 1
            high.losses = high.losses + 1
            #high.teams_played.append(low.name)
            #low.teams_played.append(high.name)
            temp_win.append(low)
            temp_lose.append(high)
        #print("Results:", high.wins, low.wins)
        games_played = games_played + 1
    if(len(original_bracket) == 1):
       bye_team = original_bracket.pop()
       temp_win.append(bye_team) 
    for team in temp_lose:
        if(team.losses < 2):
            losers_bracket.append(team)
    if len(temp_win) == 1:
        winners_bracket.append(temp_win[0])
        return games_played
    else:
        games_played = games_played + bracket(temp_win)
        return games_played

        
        
games_played = 0

#num_total_teams = int(input("How many competing teams are there?"))
num_total_teams = int(input("How many teams are participating in the tournament?     "))
skill_list = []
for number in range(0, num_total_teams):
    skill_list.append(number)
#name_list = ["Ducks", "Beavers", "Hawks", "Badgers", "Griffins", "Warriors", "Rangers", "Hornets", "Bees", "Lions"]
team_list = []

for x in range(0, num_total_teams):
    random.shuffle(skill_list)
    #random.shuffle(name_list)
    #entry = Team([], 0, 0, skill_list.pop(), name_list.pop())
    entry = Team([], 0, 0, skill_list.pop())
    if len(team_list) < 1:
        team_list.append(entry)
    else:
        index = 0
        added = False
        for value in team_list:
            if entry.skill < value.skill:
                team_list.insert(index, entry)
                added = True
                break
            index  = index + 1
        if added == False:
            team_list.append(entry)
    
winners_bracket = []
losers_bracket = []

winners_results = bracket(team_list)  

games_played = games_played + winners_results
    
losers_results = bracket(losers_bracket)
  
# games_played = games_played + losers_results

games_played = games_played

final_results = bracket(winners_bracket)

games_played = games_played + final_results 

print(games_played)
