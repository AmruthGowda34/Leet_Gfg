class Solution:
    def roatOfanother(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            rotation=s1[i:]+s1[:i]
            
            if rotation==s2:
                return True
        
        return False

s1=Solution()
print(s1.roatOfanother("abcd","cdab"))