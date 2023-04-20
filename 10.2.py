n = dict()
w = list()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle: 
    words = line.split()
    if len(words)<5 or words[0] != 'From':
        continue 
    col_pos = words[5].find(':')
    hour = words[5][: col_pos]
    if hour not in n:
        n[hour] = 1
    else:
        n[hour] +=1
for key, val in list(n.items()):
    w.append((key, val))
w.sort()
for key, val in w:
    print(key,val)
