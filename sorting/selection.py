# main login is considering first element is small and comaprinfg next with that element and swaping the smallest element

l=[5,4,3,2,1]
for i in range(len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
    l[i],l[min]=l[min],l[i]

print(l)