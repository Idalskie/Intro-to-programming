total = 0.0
num = 0

while True:
    val = input("Enter a number: ")
    if val == "done":
        break
    try:
        fval = float(val)
    except:
        print("Invalid input")
        continue
    num = num + 1
    total = total + fval
print(num, total, total/num)
