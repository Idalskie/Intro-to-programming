f = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle: 
  words = line.split()
  if len(words)<3 of words[0] != 'From':
          continue
  else:
      atpos = words[1].find('@')
      domain = words[1][atpos+1:]
      if domain not in f:
          f[domain]=1
      else:
           f[domain]+=1
print(f) 

