d={}
l=[2,2,1,1,1,2,2]
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

print(max(d))