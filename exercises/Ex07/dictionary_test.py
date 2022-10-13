"""DICTIONARY!!!"""
__author__ = "730409415"
import pytest
from dictionary import invert, favorite_color, count


""" This is an KeyError test. """
with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


""" This is an edge case for the invert function """
def test_invert_edge_case() -> None:
    assert(invert({'apple': 'cat'}) == {'apple': 'cat'})


""" This is an use case for the invert function. """
def test_invert_use_case1() -> None:
    assert(invert({'apple': 'cat'}) == {'cat': 'apple'})


""" This is an use case for the invert function. """
def test_invert_use_case2() -> None:
    assert(invert({'apple': 'cat', 'dog': 'cat'}) == {'cat': 'dog'})


""" This is an edge case for the favorite_color function. """
def test_favorite_color_edge_case() -> None:
    assert(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow")


""" This is an use case for the favorite_color function. """
def test_favorite_color_use_case1() -> None:
    assert(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue")


""" This is an use case for the favorite_color function. """
def test_favorite_color_use_case2() -> None:
    assert(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Kris": "yellow"}) == "yellow")


""" This is an edge case for the count function. """
def test_count_edge_case() -> None:
    assert(count(["cat", "dog", "cat", "cat", "dog", "mouse"]) == {'cat': 3, 'dog': 2, 'mouse': 1})


""" This is an use case for the count function. """
def test_count_use_case1() -> None:
    assert(count(["cat", "dog", "cat", "cat", "dog", "mouse", "mouse", "mouse"]) == {'cat': 3, 'dog': 2, 'mouse': 3})


""" This is an use case for the count function. """
def test_count_use_case2() -> None:
    assert(count(["cat", "dog", "cat", "cat", "dog", "mouse", "mouse", "mouse"]))