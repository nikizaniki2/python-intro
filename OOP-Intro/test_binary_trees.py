from binary_trees import *

def test_add():
    tree = MyBinTree(1)
    tree.add(2)
    tree.add(-1)
    tree.add(3)
    tree.add(-15)
    assert tree.print_tree() == [3, 2, 1, -1, -15]

def test_check_even():
    tree = MyBinTree(1)
    tree.add(2)
    tree.add(-1)
    tree.add(3)
    tree.add(-15)
    assert tree.sum_even() == 1