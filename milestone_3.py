while True:
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter, enter a single alphabetical character.")