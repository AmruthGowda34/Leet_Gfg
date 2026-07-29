class Solution:
    def single_num(self,nums):
        n=0
        for i in nums:
            n^=i    
        
        return n
s1=Solution()
nums=[1,1,2,2,3,3,4]
print(s1.signal_num(nums))