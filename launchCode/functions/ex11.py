def sumTo(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)
