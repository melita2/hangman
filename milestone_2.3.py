import random

word_list = ["apple", "pineapple", "grapes", "strawberry", "mango"]
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
