def oddnum(list):
    odd=0
    for i in list:
        if i%2==0:
            odd+=1
    return odd
print(oddnum([2,3,4,5,6]))
