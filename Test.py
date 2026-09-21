import random

secret = random.randint(1, 50)
attempts = 0
max_attempts = 5
won = False

print("🎯 Number Guessing Game!")
print("Guess the secret number between 1 and 50.")
print("You have 5 attempts.\n")

while attempts < max_attempts and not won:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        won = True
        print("🎉 Correct! You guessed the number!")
        print("🏆 You win!")
    else:
        difference = abs(secret - guess)

        # Hint system
        if difference >= 20:
            print("🧊 Ice cold!")
        elif difference >= 10:
            print("🥶 Cold!")
        elif difference >= 5:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

        # Show remaining hearts
        remaining = max_attempts - attempts
        print("Remaining lives: ", end="")

        for i in range(remaining):
            print("❤️", end="")

        print("\n")

if not won:
    print("💔 Game over!")
    print("The secret number was:", secret)
