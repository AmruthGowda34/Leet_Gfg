class Solution:
    def fun(self,s):
        s=s.lower()
        size=[0]*26
        for ch in s:
            if ch not in size:
                size[ord(ch)-ord('a')]+=1
            size[ord(ch)-ord('a')]-=1
        return all(c==0 for c in size)

s1=Solution()
print(s1.fun("AmruthA"))