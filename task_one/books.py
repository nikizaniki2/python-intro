books = [
    {
        "title": "Python Tricks: A Buffet of Awesome Python Features",
        "author": "Dan Bader",
        "genre": "programming Python",
        "detail": {
            "publication_year": 2017,
            "isbn-13": 9781775093305,
            "language": "English",
            "pages": 302
        }
    },
    {
        "title": "Fluent Python: Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "genre": "programming Python",
        "detail": {
            "publication_year": 2015,
            "isbn-13": 9781491946008,
            "language": "English",
            "pages": 792
        }
    }
]

def list_books():
    key="title"
    # [i[key] for i in books] -> magic?
    values_of_key = [i[key] for i in books]
    return values_of_key


def find_book_by_title(title):
    keys_list = list_books()
    for i in range(len(keys_list)):
        if title in keys_list[i]:
            return keys_list[i]
    return None

def find_book(by_what, value):
    if by_what == "title":
        return find_book_by_title(value)
    else:
        if by_what == "author":
            return list_books_author(value)
        else:
            if by_what == "genre":
                return list_books_genre(value)
            else:
                print("Wrong selection.")
                return

def list_books_id():
    # error because isbn-13 is in details: //fixed
    nested_key="isbn-13"
    key="detail"
    values_of_key = [i[key][nested_key] for i in books]
    return values_of_key

def list_books_author(author_name):
    key="author"
    list_of_book_ids = []
    author_list = [i[key] for i in books]
    global_list_of_ids = list_books_id()
    for i in range(len(author_list)):
        if author_name in author_list[i]:
            list_of_book_ids.append(str(global_list_of_ids[i]))
    return list_of_book_ids

def list_books_genre(genre_name):
    key="genre"
    list_of_book_ids = []
    genre_list = [i[key] for i in books]
    global_list_of_ids = list_books_id()
    for i in range(len(genre_list)):
        if genre_name in genre_list[i]:
            list_of_book_ids.append(str(global_list_of_ids[i]))
    return list_of_book_ids

list_books()
print(find_book_by_title("asd"))
print(find_book("genre", "program"))
print(find_book("author", "Luciano"))
print(find_book("title", "Python"))