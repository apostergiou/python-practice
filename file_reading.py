from sys import argv

script, file = argv

target_file = open(file, 'w')

print "The contents of the file %r are:" % file
print target_file

print "Truncating the file."
target_file.truncate()

print "Give me some input:"
input = raw_input("|> ")

print "Let's write it to the file."
target_file.write(input)

print "We are finished, so we will close the file."
target_file.close()
