def square(x):
    return x**2

m = map(square,range(10))
next(m)
list(m)
[square(x) for x in range(10)]

from functools import reduce
def add(x,y):
    return x + y

reduce(add,[1,2,5,7,9])

def is_odd(n):
    return n  % 2 ==1

list(filter(is_odd,[1,2,4,6,15]))


def add(x,y):
    return x + y

import functools
add_1 = functools.partial(add,1)
add_1(10)

import itertools
g = itertools.count()
next(g)
next(g)
next(g)
auto_add_1 = functools.partial(next,g)
auto_add_1()