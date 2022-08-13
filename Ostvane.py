radius = int(input("Please Enter radius :"))
height = int(input("Please Enter height :"))  
pi = 3.14
S1 = (2 * pi * radius * height)         #S1 = masahat janebi
S2 = (pi *( radius ** 2) * height)         #S2 = hajm
S3 = S1 + (2 * pi * (radius ** 2))                  #S3 = masahat kol
print("masahat janebi = ",S1)
print("hajm           = ",S2)
print("masahat kol    = ",S3)
