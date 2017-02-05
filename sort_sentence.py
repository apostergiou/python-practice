from sys import argv

print "Enter the sentence for sorting:"
sentence = raw_input()

def sort_sentence(sentence):
    words = sentence.split(' ')
    return sorted(words)

print "The sorted sentence is: %r" % (
    sort_sentence(sentence))
