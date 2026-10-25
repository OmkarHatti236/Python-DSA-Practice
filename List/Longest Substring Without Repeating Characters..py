s="omkar"
result=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        result.append(s[i:j])
new1=[]
for e in result:
    if(len(e)==len(set(e))):
        new1.append(e)
max=0
index=0
for i in range(0,len(new1)):
    if len(new1[i])>max:
        max=len(new1[i])
        index=i
print(new1[index])
