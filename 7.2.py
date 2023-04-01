#GitHub Assignment 7.1
count = 0
spamaverage = float(0)
thislist = []
listaverage = float(0)
lineval=0

filename = input('Please enter a filename to open:, like mbox-short.txt for example.... \n')     #asks for a file and saves it to the filename variable
try:                                                            # for exercise 7.3
    filename2 = open(filename, 'r')                             #opens the file and saves the read contents to the filename2 variable
except:                                                         # for exercise 7.3
    if filename == 'junk.txt':                                  # for exercise 7.3
        print('This is not a good file name!!! What is your problem? Go home and find a REAL TEXT FILE!!!')  # for 7.3
        quit()                                                          # for exercise 7.3

for line in filename2:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):  #text being looked for in stringof line variable
        lineval = (line[20:25])                 #looks at striing positions 20 through 25
        lineval = float(lineval)
        thislist.append(lineval)
        count = count +1

#thislist.append(lineval)
listaverage = sum(thislist)
#print(thislist)
#print(listaverage)
count = float(count)
spamaverage = listaverage / count
print ('The average SPAM confidence:', spamaverage, 'in the file', filename)
#print(count)
