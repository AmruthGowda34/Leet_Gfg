class Solution:
    def isogram(self,s):
        s=s.lower()
        alph=[False]*26
        for ch in s:
            if 'a' <= ch <= 'z':
                index=ord(ch)-ord('a')
                if alph[index]:
                    return False
                alph[index]=True
        return True

s1=Solution()
print(s1.isogram("Abhi"))