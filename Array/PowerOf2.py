class Solution:
    def Power_of_two(self,n):
        # return n>0 and (n&(n-1)==0)
        
        while n%2==0:
            n//=2

        return n==1
s1=Solution()
print(s1.Power_of_two(16))
print(s1.Power_of_two(17))
