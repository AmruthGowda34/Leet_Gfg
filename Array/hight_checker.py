class Solution:
    def checkHeight(self,n):
        m=sorted(n)
        i=0
        j=0
        count=0
        while i<len(n) and j<len(m):
            if n[i]!=m[j]:
               count+=1
            i+=1
            j+=1
        return count

s1=Solution()
print(s1.checkHeight([1, 1, 4, 2, 1, 3])) 