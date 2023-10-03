a=[[1,2,3,66],[9,7,6],[6,7,4]]
b=[]
for i in range(len(a)):
    c=len(a[i])
    d = []
    for j in range(c-1,-1,-1):
        d.append(a[i][j])
    b.append(d)
print(b) 