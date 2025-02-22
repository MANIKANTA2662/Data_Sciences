import random

def guessing_game():
    print("Think of a number between 1 and 100.")
    input("Press Enter when you're ready...")

    low, high = 1, 100
    attempts = 10

    for attempt in range(1, attempts + 1):
        if low > high:  # Prevent invalid states
            print("Oops! It looks like there was a contradiction in your hints.")
            break

        guess = random.randint(low, high)
        print(f"Attempt {attempt}: Is your number {guess}?")

        feedback = input("**********************\n==>Enter 'h' if the number is higher\n==>'l' if the number is lower\n==>'c' if the guess is correct: ").strip().lower()

        if feedback == 'c':
            print(f"Yay! The system guessed your number in {attempt} attempts.")
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    else:
        print("Chances completed. The system couldn't guess your number.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
guessing_game()
