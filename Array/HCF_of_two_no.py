class Solution:
    def HCF(self,n,m):
        minimum=min(n,m)
        for i in range(minimum,0,-1):
            if n%i==0 and m%i==0:
                print(i)
                break

s1=Solution()
s1.HCF(18,24)