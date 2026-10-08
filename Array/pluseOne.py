class Solution:
    def pluse_one(self,n):
        for i in range(len(n)-1,-1,-1):
            if n[i]<9:
                n[i]+=1
                return n
            n[i]=0
        return [1]+n
s1=Solution()
print(s1.pluse_one([1,2,3]))
print(s1.pluse_one([1,2,9]))
print(s1.pluse_one([9]))


#Most significant digit