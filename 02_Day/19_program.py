import random   
num = random.choice(['rock', 'paper', 'scissors'])
user_input = input("Enter your choice (rock, paper, scissors): ").lower()
if user_input == num:
    print(f"Both chose {num}. It's a tie!")
elif (user_input == 'rock' and num == 'scissors') or (user_input == 'paper' and num == 'rock') or (user_input == 'scissors' and num == 'paper'):
    print(f"You chose {user_input} and the computer chose {num}. You win!")
elif (user_input == 'rock' and num == 'paper') or (user_input == 'paper' and num == 'scissors') or (user_input == 'scissors' and num == 'rock'):
    print(f"You chose {user_input} and the computer chose {num}. You lose!")
else:
    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
    