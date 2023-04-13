f = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle: 
  words = line.split()
  if len(words)<2 of words[0] != 'From':
          continue
  else:
      if words [1] not in f:
          f[words[1]]=1
      else:
           f[words[1]]+=1
print(f) 
