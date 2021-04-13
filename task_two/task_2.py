import logging
import time
from datetime import datetime

def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.__code__.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "TypeError: Argument %r is not %s" % (a,t)
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts
#stackoverflow paste...
# *args, **kwargs let's a func take any number of args 
# "Then it will accept an arbitrary number of positional and keyword arguments."

def encrypt(key):
    def _inner(func):
        def wrapper(*args, **kwargs):
            original_string = func()
            encrypted_string = ""
            for char in original_string:
                if char == " ":
                    encrypted_string += char
                    continue
                temp = ord(char) + key
                encrypted_string += chr(temp)
            return encrypted_string
        return wrapper
    return _inner

#DONE: log decorator.
def log(name_of_file):
    def _inner(func):
        def wrapper(*args, **kwargs):
            return_info = func()
            logging.basicConfig(filename=name_of_file, level=logging.INFO)
            logging.info('\n{} was called at {}'.format(func.__name__, datetime.now()))
            return return_info
        return wrapper
    return _inner

#DONE: performance decorator

def performance(name_of_file):
    def _inner(func):
        def wrapper(*args, **kwargs):
            return_info = func()
            logging.basicConfig(filename=name_of_file, level=logging.INFO)
            t1 = time.time()
            t2 = time.time() - t1
            logging.info('\n{} was called and took {} seconds to complete'.format(func.__name__, t2))
            return return_info
        return wrapper
    return _inner

def gt(num):
    def _inner(input):
        return input > num
    return _inner

def gt_lambda(num):
    return lambda input: input > num
    #returns func
    
gt_one_liner = lambda num: lambda input: input > num

def lt(num):
    def _inner(input):
        return input < num
    return _inner

def lt_lambda(num):
    return lambda input: input < num

lt_one_liner = lambda num: lambda input: input < num

def eq(num):
    def _inner(input):
        return num == input
    return _inner

def eq_lambda(num):
    return lambda input: input == num

eq_one_liner = lambda num: lambda input: num == input

def oftype(t):
    def _inner(input):
        return isinstance(input,t)
    return _inner

def oftype_lambda(t):
    return lambda input: isinstance(input,t)

oftype_one_liner = lambda num: lambda input: isinstance(input,t)

def present(arg):
    def _inner():
        return arg != None
    return _inner

def present_lamda(arg):
    return lambda: arg != None

present_one_liner = lambda arg: lambda: arg != None

def pred(func):
    def _inner(input):
        return func(input)
    return _inner

def pred_lambda(func):
    return lambda input: func(input)

pred_one_liner = lambda func: lambda input: func(input)

# DONE: 2 nested funcs ->
def sum():
    return lambda num_one: lambda num_two: num_one + num_two

@accepts(int,str)
def temp_func(num, character):
    return character + str(num)

@encrypt(2)
def get_low():
    return "Get get get low"

@log('log.txt')
@performance('log.txt')
def does_sleep():
    import time
    time.sleep(0.2)
    #short sleep for testing purposes.
    return