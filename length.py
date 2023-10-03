def large(h1,h2,h3):
    l1=len(a)
    l2=len(b)
    l3=len(c)
    if l1>l2 and l1>l3:
        print(a,"is larger:")
    elif l2>l1 and l2>l3:
        print(b,"is larger")
    elif l3>l1 and l3>l2:
        print(c,"is larger")
a=input("enter:")
b=input("enter:")
c=input("enter:")
large(a,b,c)
