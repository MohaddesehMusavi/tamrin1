number=int(input("Please enter a six digit number :"))
temp = number // 10
digit2 = temp % 10
temp = number // 10000
digit5 = temp % 10
sum =digit2 + digit5
print("the sum = ",sum)

