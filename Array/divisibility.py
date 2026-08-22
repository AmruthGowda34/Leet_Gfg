class Solution:
    def check_divisibility(self,n):
        temp=n
        sum=0
        prod=1
        while temp>0:
            sum+=temp%10
            prod*=temp%10
            temp//=10
        return n%(sum+prod)==0


s1=Solution()
print(s1.check_divisibility(99))