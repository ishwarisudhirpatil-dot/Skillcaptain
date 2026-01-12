
import random

user_choice = "rock"   
computer_choice = random.choice(["rock", "paper", "scissors"])

print("User choice:", user_choice)
print("Computer choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")

elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")

elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")

elif user_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")

elif user_choice == "paper" and computer_choice == "scissors":
    print("Computer wins!")

elif user_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")

else:
    print("Invalid choice")
