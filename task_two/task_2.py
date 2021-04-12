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

# TODO: Fix uses of if (lambda)
# TODO: Redo funcs with labdas, one liner, same as now but no ifs
# TODO: tests for every func

# TODO: 2 nested funcs ->

def sum():
    return lambda num_one: lambda num_two: num_one + num_two
