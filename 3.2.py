55#Get input from user for hours and verify it is a number
hrs = input("Enter hours: ")
h = hrs
try:
    h = h * 1
    h = float(h)
except:
    print("This is not a valid number, you need to learn your numbers better!!!!")
    exit()

#Get input from user for rate and verify it is a number
sr = input("Enter rate: ")
r = sr
try:
    r = r * 1
    r = float(r)

except:
    print("This is not a valid number, you need to learn your numbers better!!!!")
    exit()

if h > 40:
    reg=r * h
    opt = (h - 40.0) * (r * 0.5)
    xp = reg + opt
else:
    xp = r * h
print(xp)
