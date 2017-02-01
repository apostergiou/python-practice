from sys import argv

script, file = argv

text = open(file).read()

print "The contents of the file %r are:" % file
print text
