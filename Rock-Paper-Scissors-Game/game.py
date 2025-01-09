import random

choices = ["Rock", "Paper", "Scissors"]

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter your choice: Rock, Paper, or Scissors")
    print("Type 'Exit' to quit the game.")
    
    
    while True:
        user_choice = input("Your choice: ")
        if user_choice == "Exit":
            print("Thanks for playing! Goodbye!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win!")
        else:
            print("You lose!")

        print()  

play_game()