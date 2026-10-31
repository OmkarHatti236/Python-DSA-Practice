num1=[1,3,5,0,0,0]
num2=[2,4,6]

m=3
n=3

i=m-1
j=n-1
k= m + n - 1
while j >= 0:
    if i >= 0 and num1[i] > num2[j]:
      num1[k] = num1[i]
      k -= 1
      i -= 1
    else:
      num1[k] = num2[j]
      k -=1
      j -= 1

print(num1)