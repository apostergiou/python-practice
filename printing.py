my_town = "Trikala"
population = 700

print "My town is %s." % my_town
print "My town's population is %d." % population

print "My town is %s and it has a population of %d." % (
    my_town, population)

print "*" * 5
print "Hello %s" % 'world'

sum1 = 10
sum2 = 20
print sum1 + sum2,
print sum1
print sum2

formatter = "%r"
print formatter % (1)
print formatter % (True)
print formatter % (formatter)
print formatter % ('one')
print formatter % (
    "Hello world!"
)

print "foo\nbar"
print """
Hello world!
We shall print multiple lines!
"""

tab = "\tPrint a tab"
list = """
A list:
\t* foo
\t* bar
"""

print tab
print list
