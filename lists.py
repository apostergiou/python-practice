elements = []

print "Creating the list"

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

print "Printing the list"

i = 0
while i < 6:
    print elements[i]
    i += 1
