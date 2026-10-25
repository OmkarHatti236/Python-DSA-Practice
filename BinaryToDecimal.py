n="100"
r=n[::-1]
val=0
for i in range(len(n)):
    val+=(int(r[i])*(2**i))
print(val)
