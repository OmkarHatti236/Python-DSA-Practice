num1=[0,0,0,1,3,5]
num2=[2,4,6]

m=len(num1)
n=len(num2)

merge=[]

i=j=k=0

while i<m and j<n:
    if num1[i]==0:
        i+=1
        continue
    if num2[j]==0:
        j+=1
        continue
    if num1[i]<=num2[j]:
        merge.append(num1[i])
        i+=1
    else:
        merge.append(num2[j])
        j+=1

for i in merge:
    print(i)

# a=[]
# a[5]=0
# print(a)