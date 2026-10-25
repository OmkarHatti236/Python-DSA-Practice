grid = [[1,3],[2,2]]

n=len(grid)
element=n*n
print(element)
result={}
for i in range(1,element+1):
    result[i]=0;


for i in range(n):
    for j in range(n):
       result[grid[i][j]]+=1

print(result)

