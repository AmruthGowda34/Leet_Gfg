class Solution:
    def fun(self,arr):
        ans=0
        for i in range(1,len(arr)+2):
            ans^=i
        
        for num in arr:
            ans^=num
            
        return ans

s1=Solution()
print(s1.fun([1,2,3,4,6]))