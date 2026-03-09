#Christian Burfeind, Alan Lozoya, Isaac Fisher, Josh Eastland
#P2 Soccer Project, create program that simulates a soccer season of a team

#functions
def welcomeMessage():

    #Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message.
    #Return the name to the main program and store it in variable so it can be used throughout the program.
    print("--- The Soccer Simulation Game ---")

    print()
    user_name = input('Enter your name: ')

    print()
    print(f'Welcome {user_name} to The Soccer Simulation Game! You will be given a menu of 4 distinct options for going through the season of your new soccer team! Get started by entering the teams in your league then choosing an option from the menu and good luck!')

    return user_name


def menu():

    #Display of menu and return choice. Store in variable and use this value to determine which function to call next.
    print()
    print("--SOCCER SIMULATION MENU--")
    print("- 1 CHOOSE HOME TEAM")
    print("- 2 CHOOSE OPPONENT")
    print("- 3 PLAY GAME")
    print("- 4 FINISH SEASON")

    #Ask for the user's choice
    print()
    choice = int(input("Input your choice (1-4): "))

    #return the chosen option
    return choice

def teamSelect(prompt = "Enter team you would you like to select: "):
    #This function should receive a parameter but give it a default value if none is passed. 

    #Display list of all teams and allow the user to choose a team using a menu. 
    #For loop where each team gets printed along with corresponding number → use if statement to select team based on position in list and choice of user
    for teams in range(0, len(lstTeams)):
        print(f"{teams + 1} - {lstTeams[teams]}")
    
    bValid = False

    #actually selecting team based on integer input of user
    while bValid == False:
        try:
            iChoice = int(input((prompt)))
            teamName = lstTeams[iChoice - 1]
            bValid = True
        except:
            print("Invalid choice, please choose again")
        
    lstTeams.remove(teamName)
    
    return teamName 


"""
- Display the final record for a team.
- Receive the home team data
- Parameters = sHomeTeam, iWins, iLoss
- display information.
- print(f “{sHomeTeam} finished with a record of {iWins}-{iLoss}”)"""

def finishSeason(sHomeTeam, iWins, iLoss):
    print(f"{sHomeTeam} finished with a record of {iWins} - {iLoss}")


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

    #if homescore > return W, else return L
    if iHomeScore > iAwayScore : 
        print(f"{sHomeTeam} wins against {sAwayTeam}: {iHomeScore} - {iAwayScore}")
        return 'W'
    else :
        print(f"{sHomeTeam} losses against {sAwayTeam}: {iHomeScore} - {iAwayScore}")
        return 'L'



#PROGRAM
#variables
iWin = 0 
iLoss = 0
sHomeTeam = ''
sAwayTeam = ''
lstTeams = [] 
bContinued = True

#introduce the program to user
welcomeMessage()

iTeamCount = int(input("\nEnter number of teams: "))

for teams in range(0, iTeamCount):
    sTeam = input(f"\nInput team {teams + 1}’s name: ").upper()
    lstTeams.append(sTeam)


while bContinued == True:

    #create menu
    iChoice = menu()

    #Use if/elif statements to call the correct function based on the choice.
    if iChoice == 1:
        if sHomeTeam == '' :
            sHomeTeam = teamSelect("Select Home Team: ")
            print(f"You chose: {sHomeTeam}")
        else:
            print ("Home team already chosen.")

    elif iChoice == 2:
        sAwayTeam = teamSelect("Select Away Team: ")
        print(f"You chose: {sAwayTeam}")

    elif iChoice == 3: 
        if sAwayTeam == '' and sHomeTeam == '':
            print("You must select a home team and an opponent before you can simulate a game")
        
        else:
            #play game to record result
            sResult = playGame(sHomeTeam, sAwayTeam)  

            #if win, add to win total
            if sResult == 'W':
                iWin = iWin + 1
            #if loss, add to loss total
            else:
                iLoss = iLoss + 1
    
    
    elif iChoice == 4:
        finishSeason(sHomeTeam, iWin, iLoss)
        bContinued = False
    
    else:
        print("Invalid choice, please choose number 1-4")