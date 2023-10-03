def passw(h1):
    b=[]
    c=[]
    h=[]
    for i in h1:
        if i.isalpha():
            b.append(i)
        elif i.isdigit():
            c.append(i)
        elif i!=i.isalnum():
            h.append(i)
    d=len(h1)
    e=len(b)
    f=len(c)
    g=len(h)
    if d>=8 and e>=4 and f>=4 and g>=1:
        print("strong")
    else:
        print("week") 
         
a=input("enter")
passw(a)