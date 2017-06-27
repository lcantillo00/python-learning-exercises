from test import testEqual

def is_palindrome(text):
    # your code here
    left=0
    rigth=len(text)-1
    while left<=rigth:
        if text[left]==text[rigth]:
            return True
        else:
         return False


testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)
