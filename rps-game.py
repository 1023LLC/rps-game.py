import random

user_wins = 0
computer_wins = 0


options = ['rock', 'paper', 'scissors']


while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == 'q':
        break
        
    if user_input not in options:
        print('Please enter a valid input!')
        continue
    
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}.")
    
    
    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a Draw!")
    else:
        print('The system wins!')
        computer_wins += 1
        
print('') 
print(f"You won {user_wins} times")      
print('')
print(f"The system won {computer_wins} times")

print('')
print('')

if user_wins > computer_wins:
    print("You beat the system!")
elif user_wins < computer_wins:
    print("The system always wins!")
else:
    print('Game Ended in a Draw!')
 
print('')
   
print("GoodBye!") 