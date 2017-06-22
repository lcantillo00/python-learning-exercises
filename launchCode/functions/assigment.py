# TODO: use def to define a function called areaOfCircle which takes an argument called r
import math
    # TODO implement your function to return the area of a circle whose radius is r
def areaOfCircle(r):
    a = r**2 * math.pi
    return a

# Below are some tests which can give you an indication that your code seems to be correct.
# IMPORTANT: You should NOT include this part when you submit in Vocareum.
# When you submit, only include the function above.
from test import testEqual

t = areaOfCircle(0)
testEqual(t, 0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(100)
testEqual(t, 31415.926535897932)
t = areaOfCircle(-1)
testEqual(t, math.pi)
t = areaOfCircle(-5)
testEqual(t, 25 * math.pi)
t = areaOfCircle(2.3)
testEqual(t, 16.61902513749)
