class Solution:
    def assign_cookies(self,g,s):
        g.sort()
        s.sort()
        right=0
        left=0
        count=0
        while left<len(g) and right<len(s):
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count

s1=Solution()
g=[1,2,4,6,8]
s=[1,2,2,3,4,7]
print(s1.assign_cookies(g = [1,2], s = [1,2,3]))
print(s1.assign_cookies(g,s))