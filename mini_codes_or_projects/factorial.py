import time
start_time = time.time()
print(start_time)
n=1
fact=1
for i in range(1,n+1):
    fact*=i
print (fact)
print(f"Process finished --- {float((time.time() - start_time))} seconds ---" , )
