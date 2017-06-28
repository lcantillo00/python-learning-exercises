def sum_of_squares(list):
    totalsum=0
    for i in list:
        totalsum=totalsum + (i**2)

    return totalsum
print(sum_of_squares([2,3,4]))
