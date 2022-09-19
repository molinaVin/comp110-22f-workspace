"""EX03_wordle!!!"""
__author__ = "730409415"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(haystack: str, needle: str) -> bool:
    """Given two strings as its parameter, returns True."""
    assert len(needle) == 1
    i: int = 0
    haystack_list = list(haystack)
    while i < len(haystack_list):
        if needle == haystack_list[i]:
            return True
        i += 1
    return False


def emojified(secret_word: str, guess: str) -> str:
    """Given a single character and a word it returns a yellow or white box based on if it exists in the string or not."""
    assert len(guess) == len(secret_word)
    secret_word_list = list(secret_word)
    guess_list = list(guess)
    i: int = 0
    correct_count: int = 0
    results = []
    while i < len(secret_word):
        if guess_list[i] == secret_word_list[i]:
            results.append(GREEN_BOX)
            correct_count += 1
        elif contains_char(secret_word, guess_list[i]):
            results.append(YELLOW_BOX)
        else:
            results.append(WHITE_BOX)
        i += 1
    return ''.join(results)


def input_guess(length: int) -> str:
    """Given a length it asks the user for a guess and if that guess is the same length as the length variable it returns otherwise it keeps asking."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess: str = input(f"That wasn't {length} chars! Try again: ")
    return guess

def verify_results(results: str, secret_word: str) -> bool:
    """Given the secret word and results we determine if the length of the secret_word multiplied by the ASCII value of a green box is equal, if so they won otherwise they did not."""
    i: int = 0
    sum: int = 0
    string_list = list(results)
    while i < len(results):
        sum += ord(string_list[i])
        if sum == (len(secret_word) * 129001):
            return True
        i += 1
    return False


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    play_count: int = 0
    max_plays: int = 6
    while play_count <= max_plays:
        print(f"=== Turn {play_count}/{max_plays} ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(secret_word, guess))
        if verify_results(emojified(secret_word, guess), secret_word):
            print(f"You won in {play_count}/{max_plays} turns!")
            return None
        play_count += 1
    print(f"X/{max_plays} - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()