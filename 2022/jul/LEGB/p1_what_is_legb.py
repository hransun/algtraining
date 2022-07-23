x = 'Global'
def func():
    x = 'enclosing'
    
    def func2():
        x = 'local'
        print(x)
    func2()
print(x)
func()

x = 'Global'
def func3():
    x = 'Enclosing'
    def func2():
        return x
    return func2
var = func3()
print(var())

print(dir(__builtins__))