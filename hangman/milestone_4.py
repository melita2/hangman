import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print(f"You've already guessed {guess}. Try again.")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                break
            else:
                print("Invalid input! Please enter a single letter.")
        
    def play(self):
        print("Let's play Hangman!")
        print(f"The word has {len(self.word)} letters.")
        while self.num_lives > 0 and self.num_letters > 0:
            print(f"You have {self.num_lives} lives left.")
            print(f"Word: {' '.join(self.word_guessed)}")
            print(f"Letters guessed: {' '.join(self.list_of_guesses)}")
            self.ask_for_input()
        if self.num_lives == 0:
            print(f"Game over! The word was {self.word}.")
        else:
            print("Congratulations! You guessed the word.")

word_list = ["apple", "pineapple", "grapes", "strawberry", "mango"]
game = Hangman(word_list)
game.play()
