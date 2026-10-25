l="12 -7 45 -3 9 -12 28 -19 3 56 -21 8 -4 17 -29 6 34 -8 23 -15 2 49 -6 31 -11 7 58 -22 14 -9 27 -5 39 -18 4 62 -13 11 -2 53 -17 19 -1 47 -10 25 -14 33"
nums = [int(x) for x in l.split(" ")]
def prog1(lst):
    print(lst)
    n=len(lst)
    value=lst[0]
    final=[]
    for i in range(n):
        for j in range(i,n):
            subarray=lst[i:j+1]
            sumsubarray=sum(subarray)
            if value<sumsubarray:
                value=sumsubarray
                final=subarray
    print(f"final subarray {final} value :{value}")

def prog2(nums):
    maxi = float('-inf')
    curr = 0
    for x in nums:
        curr += x
        if curr > maxi:
            maxi = curr
        if curr < 0:
            curr = 0
    print(maxi)
    
def prog3(nums):
        max_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            
            current_sum += n
            
            if current_sum > max_sum:
                max_sum = current_sum
        print(max_sum)

prog1(nums)
        