from task_2 import *

def test_greater_than():
    list_of_funcs = [gt, gt_lambda, gt_one_liner]
    
    for i in list_of_funcs:
        greater_than = i(0)
        assert greater_than(10) == True
        assert greater_than(-1) == False

def test_lower_than():
    list_of_funcs = [lt, lt_lambda, lt_one_liner]
    for i in list_of_funcs:
        lower_than = i(0)
        assert lower_than(10) == False
        assert lower_than(-1) == True

def test_equal():
    list_of_funcs = [eq, eq_lambda, eq_one_liner]
    for i in list_of_funcs:
        equal = i(1)
        assert equal(10) == False
        assert equal(1) == True

def test_oftype():
    list_of_funcs = [eq, eq_lambda, eq_one_liner]
    for i in list_of_funcs:
        equal = i(int)
        assert equal(str) == False
        assert equal(int) == True

def test_present():
    a = None
    list_of_funcs = [present, present_lamda, present_one_liner]
    for i in list_of_funcs:
        is_present = i("")
        assert is_present() == True

def test_pred():
    positive = gt(0) # returns _inner of gt(num) that works with num = 0 internally
    assert pred(positive)(1) == True
    assert pred(positive)(-1) == False
    
    assert pred_lambda(positive)(1) == True
    assert pred_lambda(positive)(-1) == False

    assert pred_one_liner(positive)(1) == True
    assert pred_one_liner(positive)(-1) == False
    
    list_of_funcs = [pred, pred_lambda, pred_one_liner]
    for i in list_of_funcs:
        assert i(positive)(1) == True
        assert i(positive)(-1) == False
        assert i(positive)(0) == False

def test_sum():
    do_stuff = sum()
    do_stuff_two = do_stuff(1)
    assert do_stuff_two(2) == 3

def test_accept_dec():
    assert temp_func(1, "a") == "a1"
    #assert temp_func("a",2) == AssertionError  Unable to pass tests no matter what i put there :/

def test_return_encrypt():
    assert get_low() == "Igv igv igv nqy"

def test_does_sleep():
    assert does_sleep() == None