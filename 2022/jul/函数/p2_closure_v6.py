
def counter(start = 0):
    count = [start]
    def incr():
        count[0] +=1
        return count[0]
    return incr

c1 = counter(10)
print(c1())

def counter2(start =0):
    def incr():
        nonlocal start
        start +=1
        return start
    return incr

c1 = counter2(5)
print(c1())
print(c1())

c2 = counter2(50)
print(c2())
print(c2())