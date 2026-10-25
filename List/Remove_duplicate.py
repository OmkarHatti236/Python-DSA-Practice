l=[1,1,1,2,3]
i=0
for j in range(1,len(l)):
    if l[i]!=l[j]:
        i+=1
        l[i]=l[j]
print(i+1)
print(l[:i+1])