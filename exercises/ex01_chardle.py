"""EX01 - Chardle - A cute step towards Wordle!"""
__author__ = "730409415"


first_word: str = input("Enter a 5-character word: ")
if len(first_word) > 5: 
    print("Error: Word must contain 5 characters ")
    exit()

if len(first_word) < 5: 
    print("Error: Word must contain 5 characters ")
    exit()

first_character: str = input("Enter a single character: ")
if len(first_character) > 1: 
    print("Error: Character must be a single character. ")
    exit()
if len(first_character) < 1:
    print("Error: Character must be a single character. ")
    exit()

char_count: str = (sum(char == first_character for char in first_word))

print("Searching for " + first_character + " in " + first_word) 

def stringify(num: int) -> str: 
    return str(num)

if first_character == first_word[0]:
    print(first_character + " found at index 0 ")

if first_character == first_word[1]: 
    print(first_character + " found at index 1 ")

if first_character == first_word[2]: 
    print(first_character + " found at index 2 ")

if first_character == first_word[3]: 
    print(first_character + " found at index 3 ")

if first_character == first_word[4]: 
    print(first_character + " found at index 4 ")


if char_count == 0:
    print(" No instances of " + first_character + " found in " + first_word) 

if char_count == 1: 
    print(" 1 instance of " + first_character + " found in " + first_word)

if char_count == 2: 
    print(" 2 instances of " + first_character + " found in " + first_word) 
   
if char_count == 3: 
    print(" 3 instances of " + first_character + " found in " + first_word)

if char_count == 4: 
    print(" 4 instances of " + first_character + " found in " + first_word)

if char_count == 5: 
    print(" 5 instances of " + first_character + " found in " + first_word)