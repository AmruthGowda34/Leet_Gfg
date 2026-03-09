class Solution:
    def reve(self,str,l,r):
        while l<=r:
            if str[l]!=str[r]:
                return "It is not palindrome!"
            l+=1
            r-=1
        return "It is palindrome"

s1=Solution()
str="MARKRAM"
print(s1.reve(str,0,len(str)-1))