class Solution:
    def reverse_words(self,s):
        a=""
        b=""
        for i in range(len(s)):
            if s[i]!=" ":
                a+=s[i]
            if s[i]==" " or i==len(s)-1:
                a=a[::-1]
                b+=a
                if s[i]==" ":
                    b+=" "
                a=" "
        return b
s1=Solution()
print(s1.reverse_words("Amruth Gowda HI"))