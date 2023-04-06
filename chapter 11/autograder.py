import re
fname = input(" Enter a file name:")
hand = open(fname)
numlist = []
for line in hand:
    line = line.rstrip()
    extract = re.findall("[0-9]+", line) 
    if len(extract)<1:
        continue
    for i in range(len(extract)):
        num = int(extract[i])
        numlist.append(num)
print(sum(numlist))
