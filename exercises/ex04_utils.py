"""EX04_utils!!!"""
__author__ = "730409415"


def all(int_list:list, single_int) -> bool:
    """This fucntion compares a list of int's and single int and returns True if the single int is found within the list, otherwise returns False."""
    i: int = 0 
    results: int = 0
    while i < len(int_list):
        if int_list[i] == single_int:
            results += 1
        i += 1
    if int_list and results == len(int_list):
        return True 
    else: 
        return False


def max(int_list: list) -> int: 
    """This function sorts a list of int's from lowest to highest value and then returns the last index in the list."""
    if int_list:
        int_list_sorted: list = sorted(int_list)
        return int_list_sorted[len(int_list)-1]
    else:
        raise ValueError("max() arg is an empty List")


def is_equal(int_list: list, int_list_two: list) -> bool:
    """This fucntion compares two list to see if they're identical by comparing each index and seeing if they are the same. If so, return True, else, return False. """
    i: int = 0 
    results: int = 0 
    while i < len(int_list): 
        if int_list[i] == int_list_two[i]: 
            results += 1
        i += 1 
    if results == len(int_list): 
        return True 
    else: 
        return False


print(all([1, 1, 1, 1], 13))
print(max([100, 99, 98]))
print(is_equal([1, 0, 1], [1, 0, 1]))