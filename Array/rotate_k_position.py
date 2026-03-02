class Solution(object):
    def fun(self,nums,l,r):
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            return nums
s1=Solution()
nums=[3,9,5,6,7,2]    
k=int(input("Enter k:"))%len(nums)
s1.fun(nums,len(nums)-k,len(nums)-1)
s1.fun(nums,0,len(nums)-k-1)
print(s1.fun(nums,0,len(nums)-1))