def line_conf():
    b = 10
    def line(x):
        ''' this is a comment
        '''
        return 2*x + b
    return line

b = -1
my_line = line_conf()
print(my_line(5))
print(my_line.__doc__)
print(my_line.__code__.co_varnames)
print(my_line.__code__.co_freevars)
print(my_line.__closure__[0].cell_contents)

def func():
    pass
func_magic = dir(func)

class ClassA():
    pass
obj = ClassA()
obj_magic = dir(obj)

set(obj_magic) - set(func_magic)

func.__name__