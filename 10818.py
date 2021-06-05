a=[]
b=[]
for i in range(10):
    a.append(int(input()))

for k in a:
    c=k%42
    if c in b:
        pass
    else:
        b.append(c)
        
print(b)
    

