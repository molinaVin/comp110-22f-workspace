"""DICTIONARY!!!"""
__author__ = "730409415"

# First we create an empty dictionary named inverted
    # We then loop/iterate through the original dictionary that got passed to this function using (for key in dictionary)
    # If the original loop for example was { apple : cat } The key is apple, and cat is the value
    # We would add to the invert { cat : apple } resulting in the inverted list being an inverted version of the original dictionary
def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary and check to see if duplicates were removed."""    
    inverted: dict[str, str] = {}
    for key in dictionary:
        inverted.update({dictionary[key] : key})
    
    # Now we check to see if there were any duplicates. This is done by comparing the length of the original dictionary to the lenth of the inverted dictionary.
    # Example, if a list contains 2 entries, both with the same key , the length of the list originally would be 2 when it was passed to the function.
    # But since there can be no duplicates, python will remove the duplicate in processing and the length of the final dictionary (inverted) will be 1.
    # For example: If the dictionary was { apple : cat, apple : dog } the length would be 2 since you have two entries.
    # After processing the inverted dictionary would have removed the duplicate and the inverted length would be 1.
    # This is the simplest way I can think to determine if there was originally a duplicate in the dictionary.
    if len(dictionary) != len(inverted):
        raise KeyError("The length of the original dict and this inverted dict aren't the same, something was trimmed due to being a duplicate.")
    else:
        return inverted


# We first create an empty list named values_list
# Then we loop/iterate through the original dictionary that got passed to this function using (for key in dictionary)
# For each value of each key in the dictionary, we append it to the values_list
# We then return the value that was referenced the most using apparently the max evaluation function
# I don't know much about it so I'm unfamiliar, but it seems to work lol
def favorite_color(dictionary: dict[str, str]) -> str:
    """Return the most referenced value in a dictionary."""
    values_list: list[str] = []
    for key in dictionary:
        values_list.append(dictionary[key])
    return max(values_list, key=values_list.count)


# First we create an empty dictionary named counted
    # We then loop/iterate through the original list that got passed to this function using (for item in list)
    # We then say if the item (value) is already in the counted list, update it's value by 1
    # Else it's not in the list and to add it to the list with a value of 1
def count(list) -> dict[str, str]:
    """Count the number of times a value appears in a list."""
    counted: dict[str, int] = {}
    for item in list:
        if item in counted:
            counted.update({item : counted[item] + 1})
        else:
            counted.update({item : 1})
    return counted