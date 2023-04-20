n = dict()
w = list()
name = input("Enter file:")
handle = open(name)
for line in handle: 
    words = line.split()
    if len(words)<2 or words[0] != 'From':
        continue 
    else:
        if hour not in n:
            n[words[1]] = 1
        else:
            n[words[1]] +=1
for key, val in list(n.items()):
    w.append((key, val))
w.sort(reverse = True)
for key, val in w[:1]:
    print(key,val)
