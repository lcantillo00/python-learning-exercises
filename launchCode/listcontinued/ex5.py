mylist=["liliann","al","dsfdgdghrthrth","dhshhauuu"]
def countWord(mylist):
    sum=0
    for item in mylist:
        if len(item)>4:
            # print (len(item))
            sum=sum+1
        print(sum)
countWord(mylist)
