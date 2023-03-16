def chop(p):
    del p[0]
    del p[-1]
def middle(p):
    new = p[1:]
    del new [-1]
    return new
list1 = [1, 4, 10, 15]
print(list1)
print(chop(list1))
print(middle(list1))
