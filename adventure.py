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

print "You enter a dark room. There's a ghost in front of you. What do you do?"
print "1. RUN!"
print "2. Fight!"

action = raw_input("> ")

if action == "1":
    print "You are faster than the ghost. You survived!"
elif action == "2":
    print "You find some weapons nearby. Which one do you choose?"
    print "1. Sword"
    print "2. Shield"
    print "3. I will fight with my fists alone!"

    weapon = raw_input("> ")

    if action == "1":
        print "You slaughtered the ghost."
    elif action == "2":
        print "You defended against all the ghost's attacks."
    elif action == "3":
        print "You can't fight a ghost with your fists... Game over."
    else:
        print "You slip and fall. The ghost eats you. Game over."

print """
You, %s, are %s years old.
You like %s and want to be around %s.
Game over.
""" % (username, age, favorite_food, favorite_animal)
