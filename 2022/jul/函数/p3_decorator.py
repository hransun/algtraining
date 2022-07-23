def func(x):
    return x +1

new = func
print(new(1))

def decorate(func):
    def inner():
        print('in decorator')
        func()
    return inner

@decorate
def target():
    print('do something in target')

target()