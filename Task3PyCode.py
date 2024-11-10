import random

def generate_number():
    """Generates a random 4-digit number as a string."""
    return str(random.randint(1000, 9999))

def get_cows_and_bulls(secret, guess):
    """Returns the number of cows and bulls for a given guess."""
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_number()
    guesses = 0
    while True:
        guess = input("Enter a 4-digit number: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        guesses += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the correct number {secret_number}!")
            print(f"It took you {guesses} guess(es).")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

        cows, bulls = 0, 0
            
if __name__ == "__main__":
    main()
