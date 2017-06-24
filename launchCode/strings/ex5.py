from test import testEqual

def remove_all(substr,theStr):
     newstring=theStr.replace(substr,"",)
     return newstring


testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')
