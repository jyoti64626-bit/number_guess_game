import random

number = random.randint(1, 10)
attempts = 3

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")
print("You have 3 attempts.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong guess! Try again.")
            print("Attempts left:", attempts)
        else:
            print("Game Over! The correct number was", number)