print "*" * 5
print "Hello %s" % 'world'

sum1 = 10
sum2 = 20
print sum1 + sum2,
print sum1
print sum2

formatter = "%r"
print formatter % (1)
print formatter % (true)
print formatter % (formatter)
print formatter % ('one')
print formatter % (
    "Hello world!"
)
