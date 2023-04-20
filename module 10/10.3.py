import string
counts = 0
n = dict()
w = list()
name = input("Enter file:")
handle = open(name)
for line in handle:
  line = line. translate(str.maketrans('','',string.digits))
  line = line. translate(str.maketrans('','',string.punctuation))
  line = line.lower()
  words = line.split()
  for word in words:
    for letter in words:
        counts +=1
        if letter not in n:
            n[letter]=1
        else:
            n[letter]+=1
 
for key, val in list(n.items()):
    w.append((key, val / counts))
w.sort(reverse = True)
for key, val in w[:1]:
    print(key,val)
