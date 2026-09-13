class Solution:
    def common_fact(self,n,m):
        for i in range(1,min(n,m)+1):
            if n%i==0 and m%i==0:
                print(i,end=" ")
    
s1=Solution()
s1.common_fact(10,15)