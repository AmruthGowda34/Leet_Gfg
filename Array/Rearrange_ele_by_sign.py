class Solution:
    def Rearrange_ele_by_sign(self,nums):
        re=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                re[p]=nums[i]
                p+=2
            else:
                re[n]=nums[i]               
                n+=2
        return re
    
s1=Solution()    
nums=[1,2,3,-6,-4,1,-8,-7]
print(s1.Rearrange_ele_by_sign(nums))