"""EX02_one_shot_wordle!!!"""
__author__ = "730409415"

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while True:
    guess: str = (input("What is your 6-letter guess?: "))
    if (len(guess) == len(secret_word)): 
        break 
    print(f"That was not 6 letters! Try again: {guess}")

secret_list = list(secret_word)
guess_list = list(guess)
results = []
i = 0 
correct_count = 0 

while i < len(secret_word): 
    if guess_list[i] not in secret_word: 
        results.append(WHITE_BOX)
    elif guess_list[i] == secret_list[i]:
        results.append(GREEN_BOX)
        correct_count += 1
    else: 
        results.append(YELLOW_BOX)
    i += 1

print("".join(results))
if correct_count == len(secret_word): 
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!") 
