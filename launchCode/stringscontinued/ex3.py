# from test import testEqual

def reverse(text):
    w=''
    for x in text:
        w=x+w
    return w

# testEqual(reverse("happy"), "yppah")
# testEqual(reverse("Python"), "nohtyP")
# testEqual(reverse(""), "")
print(reverse("lolu"))
