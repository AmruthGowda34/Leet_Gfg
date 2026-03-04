class Solution:
    def fun(self,nums):
        d={}
        for i in range(1,len(nums)+1):
            d[i]=0
        for i in nums:
            d[i]=1
        for k,v in d.items():
            if v==0:
                return k
        return -1
        
s1=Solution()        
nums=[1,2,3,5,6]
print(s1.fun(nums))
