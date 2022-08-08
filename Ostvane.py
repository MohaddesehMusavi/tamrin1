x = input("Please Enter r :") #r = radius
x = int(x)
y = input("Please Enter h :") #h = height
y = int(y)
pi = 3.14
S1 = (2 * pi * x * y)         #S1 = masahat janebi
S2 = (pi * x * x * y)         #S2 = hajm
S3 = S1 + S2                  #S3 = masahat kol
print("masahat janebi = ",S1)
print("hajm           = ",S2)
print("masahat kol    = ",S3)
