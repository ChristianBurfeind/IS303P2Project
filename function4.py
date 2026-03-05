#isaac fisher

#empty place holder list
lstTeams = []

#create function that generates score for 2 teams playing, chooses winner, no ties, returns W or L for main team
def playGame (sHomeTeam, sAwayTeam):
    import random
    
    iAwayScore = 0
    iHomeScore = 0 
    #generate random scores
    while iAwayScore == iHomeScore :
        #use loop to ensure no tie scores
        iAwayScore = random.randrange(1, 4)
        iHomeScore = random.randrange(1, 4)

    #remove teams from list
    if sHomeTeam in lstTeams:
        lstTeams.remove(sHomeTeam)

    lstTeams.remove(sAwayTeam)

    #if homescore > return W, else return L
    if iHomeScore > iAwayScore : 
        return f'W'
        #iWins = iWins + 1
        #dctRecord['Won Against'].append(sAwayTeam)
    else :
        return f'L'
        #iLosses = iLosses + 1
        #dctRecord['Lost Against'].append(sAwayTeam)

print(playGame('BYU', 'UTAH'))