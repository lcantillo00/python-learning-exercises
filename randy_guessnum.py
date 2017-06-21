from random import randint

num = randint(1, 6)
print ("Guess a number between 1 and 6")
answer = int(raw_input())
if answer==num:
    print ("you guess the number")
elif num<answer:
    print ("your number is less than the random #")
elif num>answer:
    print("your number is bigger than the random #")
