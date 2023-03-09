fruit = input("Enter a vegtable: ")
index = -1
nlen = len(fruit)*-1
while True:
    if index == nlen-1:
        break
    letter = fruit[index]
    print letter
    index = index-1 
