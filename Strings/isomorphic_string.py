class Solution:
    def IsoMorphic(self,s,t):
        s_to_c={}
        t_to_c={}
        
        for i in range(len(s)):
            if s[i] in s_to_c:
                if s_to_c[s[i]]!=t[i]:
                    return False
            else:
                s_to_c[s[i]]=t[i]
            
            if t[i] in t_to_c:
                if t_to_c[t[i]]!=s[i]:
                    return False
            else:
                t_to_c[t[i]]=s[i]
            
        return True
s1=Solution()
print(s1.IsoMorphic("paper","title"))
print(s1.IsoMorphic("egg","add"))
print(s1.IsoMorphic("f11","b23"))