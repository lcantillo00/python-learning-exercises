import random
def makinglist():
    randomList=[]
    for i in range(100):
        num=random.randrange(0,1001)
        randomList.append(num)
        return randomList
def average(list):
    totalcount=0
    sumtotal=0
    for i in list:
        newnum=int(i)
        sumtotal=sumtotal+i
        totalcount+=1
    sumaverg=sumtotal/totalcount
    return sumaverg
list=makinglist()
print(average(list))
    
