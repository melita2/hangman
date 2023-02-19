import random

word_list = ["apple", "grapes", "mango", "strawberry", "pineapple"]
word = random.choice(word_list)
print(word)

user_input = input("Enter a letter: ")

if len(user_input) == 1 and user_input.isalpha():
    print("Good guess!")
else:
    print("Oops! That's not valid input.")
