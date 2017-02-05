from sys import argv
from os.path import exists

script, from_file, to_file = argv

copy_text = open(from_file).read()

print "Check if the output file exist: %r" % exists(to_file)

open(to_file, 'w').write(copy_text)

