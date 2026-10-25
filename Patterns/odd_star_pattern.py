
import time
start_time = time.time()



def patern(n):
    for i in range(n):
        print(" "*(n-i),end='')
        print("*"*((2*i)-1))

n=int(input("Enter The Number Of Lines:"))+1
patern(n)
print(f"Process finished --- {int((time.time() - start_time))} seconds ---" , )
