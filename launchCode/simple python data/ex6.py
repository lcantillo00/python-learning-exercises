
P = 10000
n = 12
r = 0.08

t = int(input("Compound for how many years? "))

final = P * ( ((1 + (r/n)) ** (n * t)) )

print ("The final amount after", t, "years is", final)
