# from test import testEqual

def mirror(text):
    # your code here
    newstring=text+ reverse(text)
    return newstring

def reverse(text):
    w=''
    for x in text:
        w=x+w
        return w



# Don't copy these tests into Vocareum

print(mirror('good'))
print(mirror('Python'))
# testEqual(mirror(''), '')
# testEqual(mirror('a'), 'aa')
