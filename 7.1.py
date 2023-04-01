#GitHub Assignment 7.1
fhand = open('mbox-short.txt', 'r')
for butter in fhand:            #saves the contents of the file to 'butter'
    butter = butter.upper()     #Converts what is in the 'butter' varible to UPPER CASE
    print(butter)  
