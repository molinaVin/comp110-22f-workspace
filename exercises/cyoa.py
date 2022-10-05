"""CYAOA!!!"""
__author__ = "730409415"


"""These are needed for the clear_console function and the random number generator."""
import os, random


"""These are global variables we'll use throughout the game."""
emoji_cop = "\U0001F46E"
emoji_paper = "\U0001F4C4"
emoji_scissors = "\U00002702"
emoji_player = "\U0001F62C"
emoji_lights = "\U0001F6A8"
emoji_thuglife = "\U0001F60E"
linebreak: str = f"-------------------------------------------------------{emoji_cop}{emoji_paper}{emoji_scissors}-------------------------------------------------------"


def main() -> None:
    """This is the main entry point to the game, it will continue to run until the user quits or escapes."""
    global points
    global attempts_to_run
    points = 0
    attempts_to_run = 0
    stops: int = 0
    greet()
    while True:
        print(linebreak)
        print(f"{emoji_lights}{emoji_lights}{emoji_lights}{emoji_lights} UH OH YOU JUST GOT PULLED OVER, WHAT DO YOU DO?!{emoji_lights}{emoji_lights}{emoji_lights}{emoji_lights}")
        print("1) Try your luck and guess!")
        print("2) Make a run for it!")
        print("3) Drive away with the tickets you currently have.")
        selection: int = input("Please select an option: ")
        if int(selection) < 4:
            if selection == "1":
                stops += 1
                points = guess(points)
            elif selection == "2":
                if stops == 0:
                    stops += 1
                run()
            else:
                print(linebreak)
                if stops == 0:
                    print(f"{emoji_cop} Cop: You didn't even try to guess the number, here's your ticket!")
                    points += 1
                    stops += 1
                if points == 0:
                    print(f"Congratulations {name}, even after being stopped {stops} times you drove away with no tickets!")
                else:
                    print(f"You got {points} tickets after being stopped {stops} times, and fleeing {attempts_to_run} times {name}, better luck next time!")
                break
        else:
            print("Please select a valid option!")


def greet() -> None:
    """This function will greet the user, explain the rules, and ask for their name."""
    while True:
        clear_console()
        global name
        name = input("Greetings, please enter your name to begin: ")
        if name != "":
            break
    clear_console()
    print(linebreak)
    print(f"Welcome to {emoji_cop} Cop, {emoji_paper} Paper, {emoji_scissors} Scissors!")
    print(f"In this game, you'll assume the role of {name}, an innocent driver who totally wasn't speeding,")
    print("but got pulled over by a cop anyways. The cop is in a good mood and wants to play a game with you.")
    print("If you guess the number they're thinking of they'll cut you a break and cut up your ticket!")


def guess(points: int) -> int:
    """This function will ask the user to guess a number, the answer is a randomly generated int between 1 and 10. If the numbers match they get a point (or ticket) removed. Otherwise they don't."""
    points += 1
    answer: int = random.randint(1, 10)
    print(linebreak)
    print(f"{emoji_cop} Cop: Alright, let's play! I'm thinking of a number between 1 and 10, what do you think it is?")
    guess = input(f"{emoji_player} {name}: I think the number you're thinking of is... ")
    if int(guess) < 1 or int(guess) > 10:
        print(f"{emoji_cop} Cop: That's not a valid guess, you get a ticket!")
    else:
        if int(guess) == answer:
            points -= 1
            print(f"{emoji_cop} Cop: You guessed correctly! You're free to go!")
        else:
            print(f"{emoji_cop} Cop: You guessed wrong, I was thinking of {answer}, here's your ticket!")
    print(f"\nYou currently have {points} tickets.")
    return points


def run() -> None:
    """This function lets the user try to escape the cop, if they succeed they get a point (or ticket) removed, otherwise they get their current ticket value multiplied by 3."""
    global points
    global attempts_to_run
    points += 1
    print(linebreak)
    print("You've decided to run! You're not sure if you'll get away, but you're willing to take the risk!")
    print("There's a 20% chance you'll get away, but a 80% chance you'll get caught! If you get away you'll")
    print("lose all tickets you currently have, but if you get caught, your tickets will tripled!")
    print(f"Are you willing to take that risk {name}? It's not too late to back out!")
    print("1) Yes, I'm willing to take the risk!")
    print("2) No, go back and let me guess a number!")
    selection: int = input("Please select an option: ")
    if selection == "1":
        result: int = random.randint(1, 5)
        if result == 1:
            print(f"{emoji_thuglife} You got away, kind of hard to believe, but you did it {name}!")
            exit()
        else:
            attempts_to_run += 1
            points *= 3
            print(f"{emoji_cop} Cop: You got caught! Here's your tickets!")
            print(f"\nYou currently have {points} tickets.")
    return


def clear_console() -> None:
    """This function clears the console to make things prettier."""
    clear = lambda: os.system('cls')
    clear()


if __name__ == "__main__":
  main()
