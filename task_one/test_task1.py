from task1 import *
from books import *

def test_triangle():
    assert triangle_type(1,1,1) == "равностранен"
    assert triangle_type(1,1,2) == "равнобедрен"
    assert triangle_type(1,2,3) == "разностранен"

def test_anagram():
    assert is_anagram("Listen","Silent") == "ANAGRAMS"
    assert is_anagram("sadasd","vcxvxcvcx") == "NOT ANAGRAMS"

def test_evens():
    assert evens_count([1,2,3,4,5,1,2,9,4,5]) == 4

def test_word_counter():
    assert word_counter(['list','python','word',], 'word') == 1

def test_substrings():
    assert count_substrings("This is this and that is this", "this") == 2

def test_dict_generator():
    assert dict_generator(3,5) == {3:2, 4:1, 5:0}

def test_list_books():
    book_titles = ['Python Tricks: A Buffet of Awesome Python Features', 'Fluent Python: Clear, Concise, and Effective Programming']
    assert list_books() == book_titles

def test_find_book_by_title():
    assert find_book_by_title("Python") == 'Python Tricks: A Buffet of Awesome Python Features'
    assert find_book_by_title("asd") == None

def test_find_book():
    assert find_book("genre", "program") == ['9781775093305', '9781491946008']
    assert find_book("author", "Luciano") == ['9781491946008']
    assert find_book("title", "Python") == 'Python Tricks: A Buffet of Awesome Python Features'