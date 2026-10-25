# brute force
def brute(nums):
    find={}
    unique=set(nums)
    for num in unique:
        val=nums.count(num)
        find[num]=val

    print(max(find))


brute([2,2,1,1,1,2,2])


# moore algorithm
def majority(nums):
    candidate=nums[0]
    count=0
    for num in nums:
        if count==0:
            candidate=num
        count+=1 if candidate==num else 0
    return candidate


num1=[3,2,3]
num2=[2,2,1,1,1,2,2]

print(majority(num1))
print(majority(num2))