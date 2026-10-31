def twoSum(nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

num=[1,5,4,3,6,7]
index=twoSum(num,13)
print(index)