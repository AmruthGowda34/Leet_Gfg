class Solution:
    def lengthofLastword(self,s):
        words=s.split()
        return len(words[-1])
s1=Solution()
print(s1.lengthofLastword("luffy is still joyboy"))
print(s1.lengthofLastword("   fly me   to   the moon  "))
print(s1.lengthofLastword("Hello World"))