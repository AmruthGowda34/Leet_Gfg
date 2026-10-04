class Solution:
    def equiIndex(self,n):
        total_sum=sum(n)
        left_sum=0
        for i in range(len(n)):
            right_sum=total_sum-left_sum-n[i]
            
            if left_sum==right_sum:
                return i
            
            left_sum+=n[i]
        
        return -1
    

s1=Solution()
n=[1, 3, 5, 2, 2, 5, 2]
print(s1.equiIndex(n))