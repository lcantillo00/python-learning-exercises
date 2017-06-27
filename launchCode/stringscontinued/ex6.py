from test import testEqual
def remove_all(substr, the_str):
    # replace method essentially removes variable substr
    new_string = the_str.replace(substr, "")
    return new_string

# get user input for example
b_str = raw_input("What string would you like to remove from?")
a_str = raw_input("What would you like to remove from that string?")
print(remove_all(a_str, b_str))

testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')
