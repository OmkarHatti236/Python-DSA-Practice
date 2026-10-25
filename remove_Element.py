nums=[3,2,2,3]
val=3
# num = [x for x in nums if x != val]
# print(num)

i=0
for num in nums:
    if num!=val:
        nums[i]=num
        i+=1
    print(nums)
