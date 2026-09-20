class Solution:
    def countOccurence(self,s,p):
        count=0
        for i in range(len(s)-len(p)+1):
            match=True
            for j in range(len(p)):
                if s[i+j]!=p[j]:
                    match=False
                    break
            if match:
                count+=1
        return count    

s1=Solution()
print(s1.countOccurence("abababab","ab"))