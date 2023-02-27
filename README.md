# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Used python 

1. First, we imported the random module to select a word at random from a list.

import random

2. We created a list of words to choose from.

word_list = ["apple", "pineapple", "grapes", "strawberry", "mango"]

3. We used the random.choice() method to select a word at random from the list.

word = random.choice(word_list)

4. We printed the randomly selected word to the console.
print(word)

5. We asked the user to enter a single letter using the input() function and stored the user's input in a variable called guess.

guess = input("Please enter a single letter: ")

6. We created an if statement that checks whether the length of guess is equal to 1 and whether guess consists of only alphabetic characters using the len() and isalpha() functions.

if len(guess) == 1 and guess.isalpha():

7. If both conditions are met, we printed "Good guess!" to the console.

  print("Good guess!")

8. If the if statement is not true (i.e., the length of guess is not equal to 1 or it contains non-alphabetic characters), the else block will execute and print "Oops! Your guess should be a single letter in the alphabet."

else:
    print("Oops! This is not valid input.")

You should be able to input a letter and it will check you have put one letter and its from the alphabet.

9. add the check_guess function just prints out a message indicating whether the guess is correct or not, and the ask_for_input function does not return anything. Instead, it just calls the check_guess function within the loop until a valid guess is entered.