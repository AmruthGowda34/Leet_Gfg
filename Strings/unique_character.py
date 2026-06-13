class Solution:
    def fun(self,s):
        s=s.lower()
        size=[0]*26
        for ch in s:
            size[ord(ch)-ord('a')]+=1
            if size[ord(ch)-ord('a')]>1:
                return False
        return True
s1=Solution()
print(s1.fun("Abhigay"))