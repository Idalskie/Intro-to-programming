num_list = []
while True:
    try:
        num = input("Enter a number:")
        if num =="done":
            break
        if len(num) <1:
            break 
        else: 
            num = int(num)
    except:
        print("Invalid input")
        break
    num_list.append(num)
print("Maximum:" , max(num_list))
print("Minimum:" , min(num_list)) 
