from task1 import *
from books import *

both = [
{'title': 'Python Tricks: A Buffet of Awesome Python Features',
 'author': 'Dan Bader',
 'genre': 'programming Python',
 'detail': {
	 'publication_year': 2017,
	 'isbn-13': 9781775093305,
	 'language': 'English',
	 'pages': 302
	 }},
 {'title': 'Fluent Python: Clear, Concise, and Effective Programming',
 'author': 'Luciano Ramalho',
 'genre': 'programming Python',
	 'detail': {
	 'publication_year': 2015,
	 'isbn-13': 9781491946008,
	 'language': 'English',
	 'pages': 792}
 }]

single = [
{'title': 'Python Tricks: A Buffet of Awesome Python Features',
 'author': 'Dan Bader',
 'genre': 'programming Python',
 'detail': {
	 'publication_year': 2017,
	 'isbn-13': 9781775093305,
	 'language': 'English',
	 'pages': 302
	 }
    }
    ]

def test_triangle():
    assert triangle_type(1, 1, 1) == "равностранен"
    assert triangle_type(1.41, 1.41, 2) == "равнобедрен"
    assert triangle_type(3, 4, 5) == "разностранен"

def test_anagram():
    assert is_anagram("Listen","Silent") == "ANAGRAMS"
    assert is_anagram("TOP_CODER","COTO_PRODE") == "NOT ANAGRAMS"
    assert is_anagram("kilata","cvetelina_yaneva") == "NOT ANAGRAMS"
    assert is_anagram("BRADE","BEARD") == "ANAGRAMS"

def test_evens():
    assert events_count([1, 2, 4]) == 2

def test_word_counter():
    assert word_counter(['list','python','word',], 'word') == 1

def test_substrings():
    assert count_substrings("This is a test string", "is") == 2
    assert count_substrings("babababa", "baba") == 2
    assert count_substrings("Python is an awesome language to program in!", "o") == 4
    assert count_substrings("We have nothing in common!", "really?") == 0
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
    assert find_book("genre", "program") == both
    assert find_book("author", "Dan") == single
    assert find_book("title", "Python") == both