import re

rev = []
avg _ rev = 0
fname = imput("Enter a file:")
fhand = open(fname)
for line in fhand:
   line = line.rstrip()
   rev _ hold = re.findall(' ^New Revision: ([0-9.]+)',line)
   for val in rev_hold:
          val = int(val)
          rev = rev +[val]
revsum = sum(rev)
count = int(len(rev))
if count:
    avg _ rev = revsum / count
    average = int(avg_rev)
print(average)
