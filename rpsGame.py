import random
import sys

print('WELCOME TO MY GAME WORLD: ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
while True:  # The player input loop.
    print('Enter your move: (p)aper, (r)ock, (s)cissors')
    playerMove = input()
    if playerMove == 'quit':
        sys.exit()  # Quit the program.
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
        break  # Break out of the player in loop
    # Display what the player chose:
if playerMove == 'r':
    print('ROCK versus...')
elif playerMove == 'p':
    print('PAPER versus...')
elif playerMove == 's':
    print('SCISSORS versus...')
randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')
# Display the win,loss or tie
if playerMove == computerMove:
    print('It is a tie!')
elif playerMove == 'r' and computerMove == 's':
    print('Yeey,You win!')
elif playerMove == 'p' and computerMove == 'r':
    print('Okay champ,You win!')
elif playerMove == 's' and computerMove == 'p':
    print('This is your lucky day.You win!')
elif playerMove == 'r' and computerMove == 'p':
    print('The rock has been covered by the paper. Sorry,You lose!')
elif playerMove == 'p' and computerMove == 's':
    print('Oops! The paper has been cut by the scissors. You lose!')
elif playerMove == 's' and computerMove == 'r':
    print('Damn! The rock has crushed the scissors. You lose!')