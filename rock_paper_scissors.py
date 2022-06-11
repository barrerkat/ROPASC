# ROCK PAPER SCISSORS
import random

options = ['r', 'p', 's']
gameMode = True
cpuWins = 'CPU is the winner!!!!'
userWon = "Congrats, You are the winner!!!!"

print("Welcome to the game of Rock-Paper-Scissors")
print("\nEnter:\n")
print("\tR for ROCK")
print("\tP for PAPER")
print("\tS for SCISSORS\n")

print("It's game time, make your choice")



while gameMode:
    userInput = input('Enter an option: ').lower()
    if len(userInput) != 0 and userInput in options:
        computerOption = random.choice(options)
        print(f"Player ({userInput}) : CPU ({computerOption})")
        if computerOption == userInput:
                
            print("\nIt's a tie, let's play once more")
            
        else:

            if computerOption == 'r' and userInput == 's':
                print(cpuWins)    
                
            if computerOption == 'r' and userInput == 'p':
                print(userWon)

            if computerOption == 'p' and userInput == 'r':
                print(cpuWins)
                
            if computerOption == 'p' and userInput == 's':
                print(userWon)

            if computerOption == 's' and userInput == 'p':
                print(cpuWins)

            if computerOption == 's' and userInput == 'r':
                print(userWon)
            
            gameMode = False
    else:
        print('\nERROR: Enter a valid option\n')
    






