#Да се напише функция groupby(func, seq), връщаща речник. Вторият аргумент е итеруем обект. 
#Първият е функция, която връща ключовете от резултатния речник.
#За стойности се взимат списъци, съдържащи обектите от seq,
#без да се нарушава редът им, групирани по съответния ключ.    

# groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]) -> {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]} iterate

def groupby(func, seq):
    dict_return = {}
    func_return = 0
    for i in seq:
        func_return = func(i)
        if func_return not in dict_return.keys():
            dict_return[func_return] = []
        dict_return[func_return].append(i)

    
    return dict_return

#Да се напише функция-генератор iterate(func), която последователно връща функциите:
#identity, func, func.func, func.func.func... и т.н. ... 
#където identity е функцията идентитет, а . е оператор за композиране на функции

#https://realpython.com/introduction-to-python-generators/

#def double(x): return 2 * x
# i = iterate(double)
# f = next(i)
# f(3)
# -> 3 
# f = next(i) f(3) 6 f = next(i) f(3) 12 f = next(i) f(3) 24

def double(x): return 2 * x

# def iterate(double):
#     num = 1
#     bool first_run = True
#     def _inner_identity(x):
#         num = x
#         yield x 
#     def _inner_func(x):
#         yield double(x)
#     def __next__():
#         if first_run:
#             num += 1
#             yield _inner_identity
#         num += 1
#             yield double(x*num)


def iterate(func):
    count = 0

    # f(3) <==> _executor(3)
    # res --> count times calling func
    def _executor(num):
        res = num
        for i in range (0, count):
            res = func(res)
        return res

    while True:
        yield _executor
        count += 1

# compose(f, g, h)(input) <==> f(g(h(input)))
# compose(f, f, f)(input) <==> f(f(f(3)))

# zip_with
# Да се напише функция-генератор zip_with(func, *iterables), която приема функция func и променлив брой итеруеми - iterables.
# За всяко число i от 0 до дължината на най-късото итеруемо, прилага към функцията func аргументите взети от i-тата позиция.
# След това yield-ва резултата. Ако не бъдат подадени iterables - генераторът трябва да бъде празен (да има 0 елемента).

def concat3(x, y, z): return x + y + z

def zip_with(func, *iterables):
    if not iterables:
        return
    
    shortest_iterable = iterables[0]
    for i in range(len(iterables)):
        if len(shortest_iterable) > len(iterables[i]):
            shortest_iterable = iterables[i]

    curr_item = []
    i = None
    for i in range(0, len(shortest_iterable)):
        for j in range(0, len(iterables)):
            curr_item.append(iterables[j][i])
        yield func(*curr_item)
        curr_item.clear()
