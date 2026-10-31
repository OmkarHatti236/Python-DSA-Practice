def find_sub(a):
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            print(f"subarrays:{a[i:j]}")
            count+=1
        print()
    print(f"total subarray:{count}")
num=[5,4,3,2,1]
find_sub(num)