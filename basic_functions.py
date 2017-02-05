# *args takes all arguments and puts them in a args list
def print_args(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


print_args("Hello", "World")

def addition(op1, op2):
    sum = op1 + op2
    return sum

print addition(1, 2)
