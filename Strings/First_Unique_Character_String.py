class Solution:
    def FirstUniqueChar(self,s):
        freq_map={}
        for i in range(len(s)):
            freq_map[s[i]]=freq_map.get(s[i],0)+1
        
        for i in range(len(s)):
            if freq_map[s[i]]==1:
                return i
        
        return -1
    


s1=Solution()
print(s1.FirstUniqueChar( "leetcode"))
print(s1.FirstUniqueChar( "loveleetcode"))
print(s1.FirstUniqueChar( "aabb"))