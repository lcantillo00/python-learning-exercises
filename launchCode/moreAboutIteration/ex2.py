
def print_triang_num(n):
    for x in range(1, n+1):
        c=int(x * (x + 1) / 2)
        print(x, '\t',c)



print_triang_num(5)
