def line_conf():
    b = 10
    def line(x):
        return 2*x + b
    return line

my_line = line_conf()
print(my_line(5))