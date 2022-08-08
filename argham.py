number=int(input("Please enter a six digit number :"))
kh=0                        #kh = khareje ghesmat
while number > 0:
  b      = number%10        # b = baghi mande
  kh     = ( kh * 10 ) + b
  number = number // 10
D2  = kh % 100
D2  = D2 // 10
D5  = kh % 100000  
D5  = D5 // 10000
Sum = D2 + D5
print("Sum = ", Sum)



