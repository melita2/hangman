import random

word_list = ["apple", "pineapple", "grapes", "strawberry", "mango"]
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! this is not valid input.")

def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Invalid input! Please enter a single letter.")

while True:
    guess = ask_for_input()
    if check_guess(guess, word):
        break
