random_number = random.randint(1, 100)
guess = int(input("Guess the number "))

if guess > random_number:
    print("Too high!")
elif guess < random_number:
    print("Too low!")
else:
    print("Congratulations! You guessed the correct number.")
