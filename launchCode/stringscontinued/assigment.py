from test import testEqual
def mirror(text):
    # your code here
    newstr=reverse(text)
    return text+newstr

def reverse(text):
    w=''
    for x in text:
        w=x+w
    return w


# Don't copy these tests into Vocareum

testEqual(reverse("lilo"),"olil")
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')
