class Solution:
    def fact(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.fact(n-1)
        
s1=Solution()
print(s1.fact(5))