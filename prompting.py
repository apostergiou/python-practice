# print "How old are you?",
# age = raw_input()

# print "What is your name?",
# name = raw_input()

# print "%r is %r years old" % (
#     name, age)

# age = raw_input("How old are you? ")

# name = raw_input("What is your name? ")

# print "%r is %r years old" % (
#     name, age)

from sys import argv

script, var1, var2 = argv

print "script: %r, var1: %r, var2: %r" % (
    script, var1, var2)

# Run:
# $ python prompting.py Hello world
