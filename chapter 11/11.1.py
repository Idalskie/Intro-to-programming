import re
cont =0
expre = import("Enter a regular expression:")
reg = std(expre)
fname = 'mbox.txt'
for line in fhand:
    line = line.rstrip()
    if re.findall (reg,line) != []: 
          count +=1
print(fname +" had " + str(count) +" lines that matched " +reg)
