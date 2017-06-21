from random import randint

num = randint(1, 6)
print "Do you want to roll? (Y)es or (N)o"
answer = raw_input()
while answer.lower()[0] == "y":
    print ("You rolled a", num)
    print ("Roll again? (Y)es or (N)o")
    answer = raw_input()
print ("Okay. See you nextime")
