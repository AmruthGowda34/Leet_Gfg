class Solution:
    def compress(self,s):
        count=1
        result=""
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                result+=s[i]+str(count)
                count=1
        result+=s[-1]+str(count)
        return result
s1=Solution()
print(s1.compress("aaabccddd"))