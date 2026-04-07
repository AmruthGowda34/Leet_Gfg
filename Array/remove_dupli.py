class Solution:
    def fun(self,nums):
        nums.sort()
        i=0
        j=i+1
        while j<len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return nums[:i+1]

s1=Solution()
print(s1.fun([1,1,2,2,2,3,2,4,4,5]))