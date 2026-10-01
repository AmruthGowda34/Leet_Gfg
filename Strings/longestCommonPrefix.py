class Solution:
    def LonCommonPrefix(self,s):
        if len(s)==0:
            return ""
        common=""
        for i in range(len(s[0])):
            for j in range(1,len(s)):
                if i>=len(s[j]) or s[j][i]!=s[0][i]:
                    return common
            common+=s[0][i]
        
        return common
    
s1=Solution()
print(s1.LonCommonPrefix(["flower","flow","flight"]))
print(s1.LonCommonPrefix(["dog","doing","done"]))
print(s1.LonCommonPrefix([]))