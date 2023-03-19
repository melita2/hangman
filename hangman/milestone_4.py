import random

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid input! Please enter a single letter.")

word_list = ["apple", "pineapple", "grapes", "strawberry", "mango"]
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! this is not valid input.")

ask_for_input(word)


import random 


class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for letter in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []