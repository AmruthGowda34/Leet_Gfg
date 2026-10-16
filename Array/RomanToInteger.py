class Solution:
    def RomanToInt(self,s):
        roman={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        Integer=0
        for i in range(len(s)):
            if i<len(s)-1 and roman[s[i]]<roman[s[i+1]]:
                Integer-=roman[s[i]]
            else:
                Integer+=roman[s[i]]
        return Integer

s1=Solution()
s="MCMXCIV"
print(s1.RomanToInt(s))