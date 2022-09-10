"""EX02_one_shot_wordle!!!"""
__author__ = "730409415"

secret_word: str = "python"
guess: str = (input("What is your 6-letter guess?: "))

character_number = len(guess)
i: int = 6

while i != len(secret_word): 
    if character_number > len(secret_word): 
        print("That was not 6 letters! Try again: ")
    else: 
        if character_number < len(secret_word): 
            print("That was not 6 letters! Try again: ")
            