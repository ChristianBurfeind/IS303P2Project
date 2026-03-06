#Christian Burfeind, Alan Lozoya, Isaac Fisher, Josh Eastland
#P2 Soccer Project

def welcomeMessage():

    #Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message.
    #Return the name to the main program and store it in variable so it can be used throughout the program.
    print("--- The Soccer Simulation Game ---")

    user_name = input('Enter your name: ')

    print(f'Welcome {user_name} to The Soccer Simulation Game! You will be given a menu of 4 distinct options for going through the season of your new soccer team! Get started by choosing an option from the menu and good luck!')

    return user_name


def menu():

    #Display of menu and return choice. Store in variable and use this value to determine which function to call next.
    print("--SOCCER SIMULATION MENU--")
    print("- 1 CHOOSE HOME TEAM")
    print("- 2 CHOOSE OPPONENT")
    print("- 3 PLAY GAME")
    print("- 4 FINISH SEASON")

    #Ask for the user's choice
    choice = int(input("Input your choice (1-4): "))

    #return the chosen option
    return choice
