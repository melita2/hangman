while True:
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter, enter a single alphabetical character.")


word = "apple"
guess = input("Guess a letter: ")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")



def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Invalid input! Please enter a single letter.")
            
guess = ask_for_input()
check_guess(guess, "apple")
