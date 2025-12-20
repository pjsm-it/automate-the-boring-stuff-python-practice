import random

secret_number = random.randint(1, 20)
attempts = max_attempts = 5
guess = None

while guess != secret_number and attempts > 0:
    guess = int(input("Guess a number btween 1 and 20: "))
    if guess < secret_number:
        print("Higher!")
        attempts -= 1
        print(f"{guess}")
    elif guess > secret_number:
        print("Lower!")
        attempts -= 1
        print(f"{guess}")
    else:
        attempts -= 1
        guesses_used = max_attempts - attempts
        print(
            f"Congratulations! You guessed it with in {guesses_used} attempts!"
            )

if guess != secret_number:
    print(f"Game over! The secret number was {secret_number}")
