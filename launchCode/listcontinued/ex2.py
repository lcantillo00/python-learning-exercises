import random
def randList():
    for i in range(100):
        list=[]
        randnum=random.randrange(0,10001)
        list.append(randnum)
        return list

def maxNumber(list):
    myMax = list[0]
    for num in list:
        if myMax < num:
            myMax = num
    return myMax

mylist=randList()
print(maxNumber(mylist))
