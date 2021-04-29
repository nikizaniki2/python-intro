from iterators_generators import *
def test_groupby():
    assert groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]) == {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}

def test_generator():
    i = iterate(double)
    f = next(i)
    assert f(3) == 3
    f = next(i)
    assert f(3) == 6
    f = next(i)
    assert f(3) == 12
    f = next(i)
    assert f(3) == 24

def test_zip():
    assert list(zip_with(concat3)) == []
    first_names = ['John', 'Miles']
    last_names = ['Coltrane', 'Davis']
    spaces = [' '] * 2
    assert list(zip_with(concat3, first_names, spaces, last_names)) == ['John Coltrane', 'Miles Davis']
