l1=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        l1.append(s[i:j+1])

print(l1)
l2=[]
for l in l1:
    if l[::]==l[::-1]:
        l2.append(l)

index=0
ml=0
for i in range(len(l2)):
    n=len(l2[i])
    if(n>ml):
        index=i
        ml=max(ml,n)
    
print(l2)
print(l2[index])
s="babad"