import random
b="ABCDEGHIJL;MNIPQRSTUVWXYZabcdefghuklmnuioqwasrybkjdnfc123144134341!@#$$^"
a=int(input("enter no of pass:"))
c=int(input("enter lngth:"))
for i in range(a):
    passw=""
    for j in range(c):
        passw += random.choice(b)
    print(passw)