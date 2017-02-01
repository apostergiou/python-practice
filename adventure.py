from sys import argv

_, username = argv
prompt = '> '

print """
Welcome to Adventure %s.
The game is simple: Type your answers and win!
""" % (username)

print "What is your favorite food?"
favorite_food = raw_input(prompt)

print "What is your favorite animal?"
favorite_animal = raw_input(prompt)

print "How old are you %s?" % username
age = raw_input(prompt)

print """
You, %s, are %s years old.
You like %s and want to be around %s.
Game over.
""" % (username, age, favorite_food, favorite_animal)
