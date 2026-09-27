class Solution:
    def maxZeroOnces(self,n):
        pre_sum=0
        max_len=0
        first_index={0:-1}
        for i in range(len(n)):
            if n[i]==0:
                pre_sum-=1
            else:
                pre_sum+=1
            
            if pre_sum in first_index:
                length=i-first_index[pre_sum]
                
                if length>max_len:
                    max_len=length
            
            else:
                first_index[pre_sum]=i
            
        return max_len

s1=Solution()
n=[0,1,0,1,1,1,0]
print(s1.maxZeroOnces(n))